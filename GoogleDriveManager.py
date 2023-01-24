from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive 
import os.path as path

class GoogleDriveManager(object):
    """Class used to upload/download files to Google Drive"""
    def __init__(self):
        self.gauth = GoogleAuth()
       # Try to load saved client credentials
        gauth = GoogleAuth()
        filepath =  path.join(path.dirname(path.abspath(__file__)), "mycreds.txt")
        gauth.LoadCredentialsFile(filepath)
        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile(filepath)
        self.drive = GoogleDrive(gauth)


        
    def upload(self, filename: str, drive_id: str) -> None:
        if not path.exists(filename):
            print(f"Specified filename {filename} does not exist!")
            return
        gfile = drive.CreateFile({'parents': [{'id': drive_id}]})
        gfile.SetContentFile(upload_file) 
        gfile.Upload() # Upload the file.

    def download_file(self, file_name: str, drive_id: str) -> None:
        file_list = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(drive_id)}).GetList()
        for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1): 
            if file_name == file['title']:
                file.GetContentFile(file['title'])

