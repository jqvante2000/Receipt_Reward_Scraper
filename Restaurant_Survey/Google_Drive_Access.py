from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from requests import request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from apiclient import errors
from apiclient import http
import logging
from apiclient import discovery

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
image_list = []



# To list folders
def listfolders(service, filid, des):
    results = service.files().list(
        pageSize=1000, q="\'" + filid + "\'" + " in parents",
        fields="nextPageToken, files(id, name, mimeType)").execute()
    # logging.debug(folder)
    folder = results.get('files', [])
    for item in folder:
        if str(item['mimeType']) == str('application/vnd.google-apps.folder'):
            if not os.path.isdir(des+"/"+item['name']):
                os.mkdir(path=des+"/"+item['name'])
            print(item['name'])
            # LOOP un-till the files are found
            listfolders(service, item['id'], des+"/"+item['name'])
        else:
            downloadfiles(service, item['id'], item['name'], des)
            image_list_adder(service, item['id'], item['name'], des, image_list)

            print(item['name'])
    return folder


# To Download Files
def downloadfiles(service, dowid, name, dfilespath):
    request = service.files().get_media(fileId=dowid)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(dfilespath + "/" + name, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def image_list_adder(service, dowid, name, dfilespath, image_list):
    request = service.files().get_media(fileId=dowid)
    
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        done = downloader.next_chunk()
    with io.open(dfilespath + '/' + name, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
    directory_list = dfilespath.split('/')
    cwd_string = ''.join(directory_list[-1])
    image_list.append((cwd_string,fh, name))
    return image_list


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)  # credentials.json download from drive API
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API

    # Enter The Downloadable folder ID From Shared Link
    Folder_id = "'15bMyrDjWONLbaw_-PLTfQ1HtKVYx4GsQ'"

    results = service.files().list(
        pageSize=1000, q=Folder_id+" in parents", fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:

            
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                if not os.path.isdir("Folder"):
                    os.mkdir("Folder")
                bfolderpath = os.getcwd()+"/Folder/"
                if not os.path.isdir(bfolderpath+item['name']):
                    os.mkdir(bfolderpath+item['name'])

                folderpath = bfolderpath+item['name']
                listfolders(service, item['id'], folderpath)
            else:
                if not os.path.isdir("Folder"):
                    os.mkdir("Folder")
                bfolderpath = os.getcwd()+"/Folder/"
                if not os.path.isdir(bfolderpath + item['name']):
                    os.mkdir(bfolderpath + item['name'])

                filepath = bfolderpath + item['name']
                

                downloadfiles(service, item['id'], item['name'], filepath)
        print("\nList of Images (Restaurant, Image)\n", image_list, "\n")

from PIL import Image
def show_images(image_list):
    # Iterate through image list, grab second element in tuple, open image
    for restaurant_name, image, name_of_file in image_list:
        with open(name_of_file, 'wb') as f:
            img = Image.open(f)
    return img.show()
        

if __name__ == '__main__':
    print('\n\n') # for spacing in terminal
    main()
    print(show_images(image_list))