from PIL import Image
from PIL.ExifTags import TAGS
 
image = Image.open('test.jpeg')
info = image.getexif()
 
 
 
for tag, value in info.items():
         key = TAGS.get(tag)
         if key == 'Orientation':
             value == 1;

         print(key, value)
        #  if key == 'Make':
        #      print(key + ': ' + str(value))
        #  elif key == 'Model' :
        #          print(key + ': ' + str(value))
        #  elif key == 'Flash' :
        #      print(key + ': ' + str(value))