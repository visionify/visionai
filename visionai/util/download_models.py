import os
import sys
import re
import json
import argparse
from urllib.parse import urlparse
import shutil

from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # ROOT folder
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))

from util.general import LOGGER, print_args, check_requirements, file_md5, colorstr, invoke_cmd, WorkingDirectory

def safe_download_to_file(file, url, url2=None, min_bytes=1E0, error_msg=''):
    # Attempts to download file from url or url2, checks and removes incomplete downloads < min_bytes
    from util.general import LOGGER
    import torch

    file = Path(file)
    assert_msg = f"Downloaded file '{file}' does not exist or size is < min_bytes={min_bytes}"
    try:  # url1
        torch.hub.download_url_to_file(url, str(file), progress=True)
        assert file.exists() and file.stat().st_size > min_bytes, assert_msg  # check
    except Exception as e:  # url2
        if file.exists():
            file.unlink()  # remove partial downloads
        LOGGER.info(f'ERROR: {e}\nRe-attempting {url2 or url} to {file}...')
        os.system(f"curl -# -L '{url2 or url}' -o '{file}' --retry 3 -C -")  # curl download, retry and resume on fail
    finally:
        if not file.exists() or file.stat().st_size < min_bytes:  # check
            if file.exists():
                file.unlink()  # remove partial downloads
            LOGGER.info(f"ERROR: {assert_msg}\n{error_msg}")
        LOGGER.info('')

def safe_download_to_folder(
    url=None,
    dirname='.',
    overwrite=False
):
    # url & path check
    if url is None or os.path.isdir(dirname) is False:
        LOGGER.error('URL ({}) or dirname ({}) not valid'.format(url, dirname))
        return False

    # Find the path to save the model file.
    file_name = os.path.basename(urlparse(url).path)
    file_path = Path(dirname) / file_name

    # If the file exists, then skip download
    if overwrite is False and os.path.exists(file_path):
        LOGGER.info(f'{file_path} already exists, skip download.')
        return False

    # Download the URL to path
    safe_download_to_file(file_path, url)

    # If its a zip file, unzip it as well.
    if file_path.suffix == '.zip':
        shutil.unpack_archive(file_path, dirname) # unzip
        # os.remove(file_path)   # remove zip file

    return True

def download_models(
    scenarios=[],
    check_md5=False
):
    if scenarios is None or len(scenarios) == 0:
        LOGGER.error('Scenarios not specified')
        return False

    for scen in scenarios:
        model_url = scen['model_url']

        # Nothing to download
        if model_url is None:
            continue

        scen_name = scen['name']
        model_name = os.path.basename(urlparse(model_url).path)
        model_hash = scen['model_hash']
        model_folder = ROOT / 'run'
        model_file_path = Path(model_folder) / model_name

        # Check if model file exists before downloading.
        redownload = False
        if check_md5 and os.path.exists(model_file_path) and model_hash != file_md5(model_file_path):
            redownload = True
            LOGGER.warning(f'⛔ {colorstr("red", "bold", scen_name)}: Model MD5 has changed')

        # If not present or redownload, download file.
        if not os.path.exists(model_file_path) or redownload:
            LOGGER.info(f'{colorstr(model_name)}: Downloading {model_url}')
            safe_download_to_folder(url=model_url, dirname=model_folder)
            if check_md5 and model_hash != file_md5(model_file_path):
                LOGGER.error(f'⛔ {colorstr("red", "bold", model_name)}: Downloaded model file, but MD5 doesn\'t match')

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scenarios', type=str, default='scenarios.json', help='Scenarios file.json')
    parser.add_argument('--url', type=str, default=None, help='Model url (ex: https://workplaceos.blob.core.windows.net/models/ppe-detection/ppe-detection-0.0.1.pt)')
    parser.add_argument('--dirname', type=str, default='.', help='Results folder')
    parser.add_argument('--verify', action='store_true', help='Validate MD5 for downloaded files')
    opt = parser.parse_args()
    print_args(vars(opt))
    return opt

def main(opt):
    check_requirements()
    if opt.scenarios is not None:
        with open(opt.scenarios, 'r') as f:
            data = json.load(f)
        scenarios = data['scenarios']
        download_models(scenarios, opt.verify)
    else:
        safe_download_to_folder(opt.url, opt.dirname)

# Main method.
if __name__ == '__main__':
    opt = parse_opt()
    main(opt)
