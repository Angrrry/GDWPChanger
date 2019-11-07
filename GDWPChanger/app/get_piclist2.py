from os import path
def write_file(filename, t):
    dirpth = path.dirname(path.abspath(__file__))
    with open(path.join(dirpth,filename), "w") as f:
        for j in t:
            f.write(j)
            f.write("\n")
    return None

def read_file(filename):
    dirpth = path.dirname(path.abspath(__file__))
    with open(path.join(dirpth,filename), "r") as f:
        t = f.read().splitlines()
    return t

def rewrite_date(new_date):
    dirpth = path.dirname(path.abspath(__file__))
    t = read_file("confg.py")
    for i in range(len(t)):
        if "LAST_MODIFICATION_DATE" in t[i]:
            t[i] = 'LAST_MODIFICATION_DATE = "{}"'.format(new_date)
    write_file("confg.py", t)

def get_GD_list(credentials, http, service, FOLDER_NAME, FOLDER_ID=None):
    """IDK what is broken, but function only returns 100 files"""
    def getting(string_stuff, credentials, http, service):
        arr = []
        page_token = None
        while True:
            response = service.files().list(q=string_stuff, spaces='drive', \
            fields='nextPageToken, files(id, name)', pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                arr.append(file['id'])
            page_token = response.get('nextPageToken')
            if page_token is None:
                break
        return(arr)
    #Находим id папки с подходящим именем
    response = service.files().list(q='name contains "{}" and mimeType="application/vnd.google-apps.folder"'.format(FOLDER_NAME), spaces='drive', \
    fields='nextPageToken, files(id, name, modifiedTime)').execute()
    folders = response.get('files', [])
    if folders == []:
        raise ValueError("Wrong FOLDER NAME")
    elif len(folders) > 1:
        if FOLDER_ID == None:
            raise ValueError("There are more than one folder with this name")
        else:
            for i in folders:
                if i["id"] == FOLDER_ID:
                    a +=1
                    folder = i
            if not folder:
                raise ValueError("Wrond FOLDER_ID")
    else:
        folder = folders[0]
    try:
        from confg import LAST_MODIFICATION_DATE
    except:
        LAST_MODIFICATION_DATE = ''
    if LAST_MODIFICATION_DATE < folder["modifiedTime"]:
        rewrite_date(folder["modifiedTime"])
        arr = getting("mimeType='image/jpeg' and '{0}' in parents".format(folder["id"]), credentials, http, service)
        write_file("piclist.txt",arr)
        print("date updated")
        return arr
    else:
        return read_file("piclist.txt")

if __name__ == '__main__':
	print("I'm here")
