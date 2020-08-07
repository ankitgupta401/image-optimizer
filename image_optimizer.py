import sys
import os
from PIL import Image


def functionality():
    print('Starting')
    try :
       images_folder = sys.argv[1]
    
    except IndexError :
        print('Please Make Sure You Have Given Input Folder')

    if(os.path.isdir(images_folder)):
        
        arr = os.listdir(images_folder)
        
        for items in arr:
          if items != "site.webmanifest":
            file, ext = os.path.splitext(items)
            image = Image.open(images_folder + items)
            image.thumbnail((600,600), Image.ANTIALIAS)

            image.save(images_folder +file + ext,optimize=True,quality=70)
    else:
        print(f'No Folder {images_folder} ')



functionality()
