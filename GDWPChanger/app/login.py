from os import path, makedirs
from oauth2client import tools, client
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = ' https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = path.join(path.dirname(
    path.abspath(__file__)), 'client_secret.json')
APPLICATION_NAME = 'Drive API Python Quickstart'
# FOLDER_ID = '1g_j6EtVDfi0uQydXiaai1kvmz_p6inw4'
#FOLDER_ID = '1SAuEtZ-BsyRALSL1bHUjAEx3i2NWYR-P'
# Vert


def get_credentials():
    home_dir = path.expanduser('~')
    credential_dir = path.join(home_dir, '.credentials')
    if not path.exists(credential_dir):
        makedirs(credential_dir)
    credential_path = path.join(credential_dir,
                                'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

    if __name__ == '__main__':
        get_credentials()
        print("I'm here")
