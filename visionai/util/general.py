import os
import sys
import re
import platform
from datetime import datetime
import coloredlogs, logging
from typing import Optional
from subprocess import check_output, STDOUT
from logging.handlers import RotatingFileHandler
import inspect
import pkg_resources as pkg
import hashlib
import time
import contextlib
import yaml


from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # edge-inference ROOT folder
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH

from util import TryExcept, emojis, WorkingDirectory

def invoke_cmd(cmd):
    try:
        output = check_output(cmd, shell=True, stderr=STDOUT).decode()
    except Exception as ex:
        output = str(ex.output)
    return output

def is_ascii(s=''):
    # Is string composed of all ASCII (no UTF) characters? (note str().isascii() introduced in python 3.7)
    s = str(s)  # convert list, tuple, None, etc. to str
    return len(s.encode().decode('ascii', 'ignore')) == len(s)

class NoColorFormatter(logging.Formatter):
    ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')  # Regex for ansi strings
    MILLI_RE = re.compile(r'(:\d\d),\d\d\d') # Regex for millisec removal
    def format(self, record):
        s = super().format(record)
        s = re.sub(self.ANSI_RE, '', s)
        s = re.sub(self.MILLI_RE, r'\1', s)
        # s = s.encode('ascii', 'ignore').decode()  # Remove emojis
        return s

def create_logger() -> logging.Logger:
    # Use /var/log folder, if not accessible use local
    LOGFILE = '/var/log/vfyapp.log'
    if not os.access(LOGFILE, os.W_OK):
        LOGFILE = ROOT / 'vfyapp.log'
    FORMAT = "%(asctime)s %(filename)20s:%(lineno)3d [%(levelname).3s] %(message)s"
    coloredlogs.install(level='INFO', fmt=FORMAT)

    # Disable azure debug logging
    logging.getLogger('azure').setLevel(logging.WARNING)

    # Create a logger object.
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    # Output to File (Max log size is 100KB)
    file_hdlr = RotatingFileHandler(LOGFILE, maxBytes=100000, backupCount=3)
    file_hdlr.setLevel(logging.INFO)
    file_hdlr.setFormatter(NoColorFormatter(FORMAT))
    log.addHandler(file_hdlr)
    return log

# Static initialization
LOGGER = create_logger()

def check_python(minimum='3.7.0'):
    # Check current python version vs. required python version
    check_version(platform.python_version(), minimum, name='Python ', hard=True)

def check_version(current='0.0.0', minimum='0.0.0', name='version ', pinned=False, hard=False, verbose=False):
    # Check version vs. required version
    current, minimum = (pkg.parse_version(x) for x in (current, minimum))
    result = (current == minimum) if pinned else (current >= minimum)  # bool
    s = f'WARNING ⚠️ {name}{minimum} is required by YOLOv5, but {name}{current} is currently installed'  # string
    if hard:
        assert result, emojis(s)  # assert min requirements met
    if verbose and not result:
        LOGGER.warning(s)
    return result

@TryExcept()
def check_requirements(requirements=ROOT / 'requirements.txt', exclude=(), install=True, cmds=''):
    # Check installed dependencies meet our inference requirements (pass *.txt file or list of packages or single package str)
    prefix = colorstr('red', 'bold', 'requirements:')
    check_python()  # check python version
    if isinstance(requirements, Path):  # requirements.txt file
        file = requirements.resolve()
        assert file.exists(), f"{prefix} {file} not found, check failed."
        with file.open() as f:
            requirements = [f'{x.name}{x.specifier}' for x in pkg.parse_requirements(f) if x.name not in exclude]
    elif isinstance(requirements, str):
        requirements = [requirements]

    s = ''
    n = 0
    for r in requirements:
        try:
            pkg.require(r)
        except (pkg.VersionConflict, pkg.DistributionNotFound):  # exception if requirements not met
            s += f'"{r}" '
            n += 1

    if s and install:  # check environment variable
        LOGGER.info(f"{prefix} VISIONAI requirement{'s' * (n > 1)} {s}not found, attempting AutoUpdate...")
        try:
            # assert check_online(), "AutoUpdate skipped (offline)"
            LOGGER.info(check_output(f'pip3 install {s} {cmds}', shell=True).decode())
            source = file if 'file' in locals() else requirements
            s = f"{prefix} {n} package{'s' * (n > 1)} updated per {source}\n" \
                f"{prefix} ⚠️ {colorstr('bold', 'Restart runtime or rerun command for updates to take effect')}\n"
            LOGGER.info(s)
        except Exception as e:
            LOGGER.warning(f'{prefix} ❌ {e}')

def clean_str(s):
    # Cleans a string by replacing special characters with underscore _
    return re.sub(pattern="[|@#!¡·$€%&()=?¿^*;:,¨´><+]", repl="_", string=s)

def colorstr(*input):
    # Colors a string https://en.wikipedia.org/wiki/ANSI_escape_code, i.e.  colorstr('blue', 'hello world')
    *args, string = input if len(input) > 1 else ('blue', 'bold', input[0])  # color arguments, string
    colors = {
        'black': '\033[30m',  # basic colors
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bright_black': '\033[90m',  # bright colors
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'bright_white': '\033[97m',
        'end': '\033[0m',  # misc
        'bold': '\033[1m',
        'underline': '\033[4m'}
    return ''.join(colors[x] for x in args) + f'{string}' + colors['end']

def print_args(args: Optional[dict] = None, show_file=True, show_func=False):
    # Print function arguments (optional args dict)
    x = inspect.currentframe().f_back  # previous frame
    file, _, func, _, _ = inspect.getframeinfo(x)
    if args is None:  # get args automatically
        args, _, _, frm = inspect.getargvalues(x)
        args = {k: v for k, v in frm.items() if k in args}
    try:
        file = Path(file).resolve().relative_to(ROOT)
    except ValueError:
        file = Path(file).stem
    s = (f'{file}: ' if show_file else '') + (f'{func}: ' if show_func else '')
    LOGGER.info(colorstr(s) + ', '.join(f'{k}={v}' for k, v in args.items()))

def file_age(path=__file__):
    # Return days since last file update
    dt = (datetime.now() - datetime.fromtimestamp(Path(path).stat().st_mtime))  # delta
    return dt.days  # + dt.seconds / 86400  # fractional days

def file_date(path=__file__):
    # Return human-readable file modification date, i.e. '2021-3-26'
    t = datetime.fromtimestamp(Path(path).stat().st_mtime)
    return f'{t.year}-{t.month}-{t.day}'

def file_size(path):
    # Return file/dir size (MB)
    mb = 1 << 20  # bytes to MiB (1024 ** 2)
    path = Path(path)
    if path.is_file():
        return path.stat().st_size / mb
    elif path.is_dir():
        return sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / mb
    else:
        return 0.0

def file_md5(path):
    path = Path(path)
    if path.is_file():
        hash_md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    else:
        return None

def check_online():
    # Check internet connectivity
    import socket

    def run_once():
        # Check once
        try:
            socket.create_connection(("1.1.1.1", 443), 5)  # check host accessibility
            return True
        except OSError:
            return False

    return run_once() or run_once()  # check twice to increase robustness to intermittent connectivity issues

@TryExcept()
@WorkingDirectory(ROOT)
def git_describe(path=ROOT):
    # Return software version
    try:
        assert (Path(path) / '.git').is_dir()
        return check_output(f'git -C {path} describe', shell=True).decode()[:-1]
    except Exception:
        return ''

def get_system_version():
    return git_describe()

@TryExcept()
@WorkingDirectory(ROOT)
def check_git_status(repo='visionify/edge-inference', branch='main'):
    # edge-inference status check, recommend 'git pull' if code is out of date
    url = f'git@github.com:{repo}.git'
    msg = f', for updates see {url}'
    s = colorstr('github: ')  # string
    assert Path('.git').exists(), s + 'skipping check (not a git repository)' + msg
    assert check_online(), s + 'skipping check (offline)' + msg

    splits = re.split(pattern=r'\s', string=check_output('git remote -v', shell=True).decode())
    matches = [repo in s for s in splits]
    if any(matches):
        remote = splits[matches.index(True) - 1]
    else:
        remote = 'ultralytics'
        check_output(f'git remote add {remote} {url}', shell=True)
    check_output(f'git fetch {remote}', shell=True, timeout=5)  # git fetch
    local_branch = check_output('git rev-parse --abbrev-ref HEAD', shell=True).decode().strip()  # checked out
    n = int(check_output(f'git rev-list {local_branch}..{remote}/{branch} --count', shell=True))  # commits behind
    if n > 0:
        pull = 'git pull' if remote == 'origin' else f'git pull {remote} {branch}'
        s += f"⚠️ YOLOv5 is out of date by {n} commit{'s' * (n > 1)}. Use `{pull}` or `git clone {url}` to update."
    else:
        s += f'up to date with {url} ✅'
    LOGGER.info(s)

@WorkingDirectory(ROOT)
def check_git_info(path=ROOT):
    # YOLOv5 git info check, return {remote, branch, commit}
    check_requirements('gitpython')
    import git
    try:
        repo = git.Repo(path)
        remote = repo.remotes.origin.url  # i.e. 'git@github.com:visionify/edge-inference.git'
        commit = repo.head.commit.hexsha  # i.e. '15b5ee18eb2206d3f9b9b40ea8fe31e43607d8d4'
        try:
            branch = repo.active_branch.name  # i.e. 'main'
        except TypeError:  # not on any branch
            branch = None  # i.e. 'detached HEAD' state
        return {'remote': remote, 'branch': branch, 'commit': commit}
    except git.exc.InvalidGitRepositoryError:  # path is not a git dir
        return {'remote': None, 'branch': None, 'commit': None}

def gpu_mem_stats():
    if platform.system() == 'Darwin':

        # Mac OS - nvidia-smi is not supported.
        check_requirements('psutil', install=True)
        import psutil
        mem = psutil.virtual_memory()

        used_pct_s = f'{mem.used/mem.total * 100:.1f}'
        used_gb_s = f'{mem.used/1024/1024/1024:.0f}'
        total_gb_s = f'{mem.total/1024/1024/1024:.0f}'

        mem_free_pct = mem.available/mem.total * 100
        free_pct_s = f'{mem_free_pct:.1f}'
        free_gb_s = f'{mem.available/1024/1024/1024:.0f}'

        color = 'cyan' if mem_free_pct > 30 else 'red'
        check = '✅' if mem_free_pct > 30 else '❌'

        LOGGER.info(colorstr(color, f'{check} CPU memory [USED]: {used_pct_s}% [{used_gb_s}GB/{total_gb_s}GB]'))
        LOGGER.info(colorstr(color, f'{check} CPU memory [FREE]: {free_pct_s}% [{free_gb_s}GB/{total_gb_s}GB]'))
        return mem_free_pct

    else:
        check_requirements('nvidia-ml-py3', install=True)
        import nvidia_smi

        def sizeof_fmt(num, suffix="B"):
            for unit in ["", "K", "M", "G", "T"]:
                if abs(num) < 1024.0:
                    return f"{num:3.1f}{unit}{suffix}"
                num /= 1024.0
            return f"{num:.1f}Yi{suffix}"

        nvidia_smi.nvmlInit()
        deviceCount = nvidia_smi.nvmlDeviceGetCount()
        for i in range(deviceCount):
            handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
            info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
            dev = nvidia_smi.nvmlDeviceGetName(handle).decode('utf-8')
            mem_free_pct = 100*info.free/info.total
            color = 'cyan' if mem_free_pct > 30 else 'red'
            check = '✅' if mem_free_pct > 30 else '❌'
            mem_free_pct_s = f'{mem_free_pct:.2f}% free'
            mem_total_s = f'{sizeof_fmt(info.total)}'
            mem_used_s = f'{sizeof_fmt(info.used)}'
            LOGGER.info(colorstr(color, f'{check} GPU {i} [{dev}]: {mem_free_pct_s} [{mem_used_s}/{mem_total_s}]'))

        nvidia_smi.nvmlShutdown()
        return mem_free_pct


class Profile(contextlib.ContextDecorator):
    # YOLOv5 Profile class. Usage: @Profile() decorator or 'with Profile():' context manager
    def __init__(self, t=0.0):
        self.t = t

    def __enter__(self):
        self.start = self.time()
        return self

    def __exit__(self, type, value, traceback):
        self.dt = self.time() - self.start  # delta-time
        self.t += self.dt  # accumulate dt

    def reset(self):
        self.t = 0

    def time(self):
        return time.time()



def copy_attr(a, b, include=(), exclude=()):
    # Copy attributes from b to a, options to only include [...] and to exclude [...]
    for k, v in b.__dict__.items():
        if (len(include) and k not in include) or k.startswith('_') or k in exclude:
            continue
        else:
            setattr(a, k, v)

def increment_path(path, exist_ok=False, sep='', mkdir=False):
    # Increment file or directory path, i.e. runs/exp --> runs/exp{sep}2, runs/exp{sep}3, ... etc.
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')

        # Method 1
        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'  # increment path
            if not os.path.exists(p):  #
                break
        path = Path(p)

        # Method 2 (deprecated)
        # dirs = glob.glob(f"{path}{sep}*")  # similar paths
        # matches = [re.search(rf"{path.stem}{sep}(\d+)", d) for d in dirs]
        # i = [int(m.groups()[0]) for m in matches if m]  # indices
        # n = max(i) + 1 if i else 2  # increment number
        # path = Path(f"{path}{sep}{n}{suffix}")  # increment path

    if mkdir:
        path.mkdir(parents=True, exist_ok=True)  # make directory

    return path

def yaml_load(file='data.yaml'):
    # Single-line safe yaml loading
    with open(file, errors='ignore') as f:
        return yaml.safe_load(f)


def yaml_save(file='data.yaml', data={}):
    # Single-line safe yaml saving
    with open(file, 'w') as f:
        yaml.safe_dump({k: str(v) if isinstance(v, Path) else v for k, v in data.items()}, f, sort_keys=False)



if __name__ == '__main__':
    # Some logging examples.
    LOGGER.debug("this is a debugging message")
    LOGGER.info("this is an informational message")
    LOGGER.warning("this is a warning message")
    LOGGER.error("this is an error message")
    LOGGER.critical("this is a critical message")

    # Testing file utilities.
    LOGGER.info('File age: {}'.format(file_age(__file__)))
    LOGGER.info('File date: {}'.format(file_date(__file__)))
    LOGGER.info('File size: {}'.format(file_size(__file__)))


    # Testing if system is online
    LOGGER.info('System Online: {}'.format(check_online()))

    # Testing Software version
    LOGGER.info('Software version: {}'.format(git_describe()))

    # Testing git info
    LOGGER.info('git info: {}'.format(check_git_info()))

    # Testing git update
    LOGGER.info('git status: {}'.format(check_git_status()))

    # Testing gpu/memory status
    LOGGER.info('GPU Memory: {:.2f}%'.format(gpu_mem_stats()))

    # Testing profiler
    dt = Profile(), Profile(), Profile()
    seen = 0
    for idx in range(20):
        with dt[0]:
            # do processing for dt0
            time.sleep(0.01)

        with dt[1]:
            # do processing for dt1
            time.sleep(0.02)

        with dt[2]:
            # do processing for dt1
            time.sleep(0.03)

        seen += 1

        # Print time (inference-only)
        LOGGER.info(f"{dt[1].dt * 1E3:.1f}ms")

    # Print results
    t = tuple(x.t / seen * 1E3 for x in dt)  # speeds per image
    LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms postprocess' % t)
