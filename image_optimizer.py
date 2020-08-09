import sys
import os
from PIL import Image,UnidentifiedImageError


def functionality():
    print('Starting')
  
for folders in range(1, len(sys.argv)):
   #  print(len(sys.argv))
    try :
       images_folder = sys.argv[folders]
       print(images_folder)
    except IndexError :
        print('Please Make Sure You Have Given Input Folder')

    if(os.path.isdir(images_folder)):
           arr = os.listdir(images_folder)
        
           for items in arr:
                 if items != "site.webmanifest":
                    try :
                      file, ext = os.path.splitext(items)
                      image = Image.open(images_folder + items)
                      image.thumbnail((600,600), Image.ANTIALIAS)
                      image.save(images_folder +file + ext,optimize=True,quality=95)
                    except UnidentifiedImageError: 
                      continue
    else:
       print(f'No Folder {images_folder} ')



functionality()
