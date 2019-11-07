from io import FileIO
from apiclient.http import MediaIoBaseDownload

def download_file(service, file_id, filename):
	request = service.files().get_media(fileId=file_id)
	fh = FileIO(filename, 'wb')
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
		status, done = downloader.next_chunk()
if __name__ == '__main__':
    #is_connected()
    print("I'm here")
