import facebook
import os

albumId = ''
access_token = ''

fb = facebook.GraphAPI(access_token, 12.0)

#Ordner aus dem die Bilder hochgeladen werden sollen.
directory = r''

while(True):
    for filename in os.listdir(directory):
        #Für Videos oder andere Bildformate die Endungen ändern oder andere hinzufügen.
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".JPG"):
            path = os.path.join(directory, filename)
            #Als Album_path die Id des Albums/photos.
            fb.put_photo(open(path, "rb"),album_path="{}/photos".format(albumId) , message=filename)

            #Nachdem die Bilder hochgeladen wurden werden sie in den Ordner abgelegt,
            os.replace(path, os.path.join(r"PicturesToUpload\SynchedPics", filename))
            print(filename + " was uploaded.")