# -*- coding: utf-8 -*-
from confg import FOLDER_NAME, FOLDER_ID
from connection import is_connected


def main():
    # Нужно было для проверки адреса интерпретатора python
    # import sys
    # print(sys.executable)
    from login import get_credentials
    from get_piclist2 import get_GD_list
    from download import download_file
    from WP import setWP
    from os import path, makedirs
    from httplib2 import Http
    from apiclient import discovery
    from random import randint

    """НЕ БУДЕТ РАБОТАТЬ. НАДО ПЕРЕПИСАТЬ get_GD_list.
    Сейчас он смотрит на дату изменения, и грузит список для горизонтальных пикч."""
    SCOPES = ' https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = path.join(path.dirname(
        path.abspath(__file__)), 'client_secret.json')
    APPLICATION_NAME = 'Drive API Python Quickstart'

    credentials = get_credentials()
    pth = path.dirname(path.abspath(__file__))
    http = credentials.authorize(Http())
    service = discovery.build('drive', 'v3', http=http)
    FOLDER_NAME = "Vert"
    FOLDER_ID = "1A2BDig0NL5jYBtnIrXcEAQmn1XDD2rWR"
    ids = get_GD_list(credentials, http, service,
                      FOLDER_NAME, FOLDER_ID=FOLDER_ID)
    print(len(ids))
    wppath = path.join(pth, "sync", "Vert.txt")
    with open(wppath, "w") as f:
        f.write('\n'.join(ids))

    # fileId = ids[randint(0, len(ids))]
    download_file(service, ids[0], path.join(pth, "sync", "1.jpg"))
# setWP(wppath)


if __name__ == '__main__':
    from time import sleep
    while is_connected() == False:
        print("fucked")
        sleep(60)
    main()
