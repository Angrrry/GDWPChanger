# -*- coding: utf-8 -*-
from connection import is_connected
import sys


def main():
    from login import get_credentials
    from get_piclist2 import get_GD_list
    from download import download_file
    from WP import setWP
    from os import path, makedirs
    from httplib2 import Http
    from apiclient import discovery
    from random import randint

    from confg import FOLDER_NAME, FOLDER_ID
    SCOPES = ' https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = path.join(path.dirname(
        path.abspath(__file__)), 'client_secret.json')
    APPLICATION_NAME = 'Drive API Python Quickstart'

    credentials = get_credentials()
    pth = path.dirname(path.abspath(__file__))
    http = credentials.authorize(Http())
    service = discovery.build('drive', 'v3', http=http)
    ids = get_GD_list(credentials, http, service, FOLDER_NAME)
    fileId = ids[randint(0, len(ids))]
    wppath = path.join(pth, "wallpaper.jpg")
    download_file(service, fileId, wppath)
    setWP(wppath)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        from time import sleep
        while is_connected() == False:
            print("fucked")
            sleep(60)
        main()
    elif sys.argv[1] = "upload":
        path = sys.argv[2]
        print("Пока ни хера не готово")
