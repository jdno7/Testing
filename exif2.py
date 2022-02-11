from exif import Image




img = Image('new_img.jpeg')
    
# img.orientation = 1

print(img.orientation)

# new_img = open('new_img.jpeg','wb')

#save new img with modified data
# with open(f'modified_{img_filename}', 'wb') as new_image_file:
#         new_image_file.write(img.get_file())