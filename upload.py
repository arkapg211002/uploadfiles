from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
gauth=GoogleAuth()
gauth.LocalWebserverAuth()
drive=GoogleDrive(gauth)
path=r"D:\OneDrive\Documents\competitive-programming-pdf-9909-12668.pdf"
for x in os.listdir(path):
    f=drive.CreateFile({'pdf':x})
    f.SetContentFile(os.path.join(path,x))
    f.Upload()
    f=None