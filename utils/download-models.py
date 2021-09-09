import os
import urllib.request
from azure.cosmosdb.table.tableservice import TableService
import dotenv


home_dir = os.path.join(os.path.expanduser('~'), '.visionai')
dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
cs = os.environ.get('visionai_connection_str')
base_url = os.environ.get('visionai_base_url')

def query_models_for_user(user, model_name):
    table_service = TableService(connection_string=cs)
    models = table_service.query_entities('models', filter="PartitionKey eq 'models' and user eq '{}' and modelname eq '{}'".format(user, model_name), select='modelfile,protofile,labels')
    # for model in models:
    #     print(model.user, model.modelname, model.modelfile, model.protofile, model.labels)
    return models

def download_model(model):
    '''
    This is utility method to figure out which model to download.
    For now, this is directly using Azure tables. Later we need to
    move this behind an API & anonymize+authenticate access to models.

    :param model: name of model (ex: visionai/SSD-Mobilenet-V2)
    :return: Directory where the model is downloaded.
    '''

    # First convert the model_name into user + model
    user, model_name = model.split('/')
    models = query_models_for_user(user, model_name)
    for model in models:
        print(model.modelfile, model.protofile, model.labels)
        print('Downloading models.')

        user_dir = os.path.join(home_dir, 'models', user)
        os.makedirs(user_dir, exist_ok=True)
        model_dir = os.path.join(user_dir, model_name)
        os.makedirs(model_dir, exist_ok=True)

        model_file_url = f'{base_url}/{user}/{model.modelfile}'
        model_protofile_url = f'{base_url}/{user}/{model.protofile}'
        model_labels_url = f'{base_url}/{user}/{model.labels}'

        # Download files
        print('.. Downloading model file {}: {}'.format(model.modelfile, model_file_url))
        urllib.request.urlretrieve(model_file_url, os.path.join(model_dir, model.modelfile.split('/')[1]))

        print('.. Downloading model prototxt file {}: {}'.format(model.protofile, model_protofile_url))
        urllib.request.urlretrieve(model_protofile_url, os.path.join(model_dir, model.protofile.split('/')[1]))

        print('.. Downloading model labels file {}: {}'.format(model.labels, model_labels_url))
        urllib.request.urlretrieve(model_labels_url, os.path.join(model_dir, model.labels.split('/')[1]))

        print('Download complete.')
        break


if __name__ == '__main__':
    download_model('arunima/SSD-MobilenetV2-colors')
