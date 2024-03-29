##=====================================================##
##        File: crop_images.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-08-16
##     Updated: 2023-08-16
##       About: Takes a rootpath and crops all images
##              (with specified extensions) in all sub-
##              directories from rootpath.
##=====================================================##

from PIL import Image
import os



# CHANGE THESE FOR YOUR CASE #
rootpath_for_conversion = 'C:\\MASTER-THESIS\\REPORT\\FIGURES\\Coin cell assembly' # remember to write '\\' for every '\'
current_extension = '.jpg' 

# crop image with values as the corners of a rectangular region in the image (values in pixels) # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop
crop_left = 1170
crop_top = 970
crop_width =  900
crop_height = 600
crop_right = crop_left + crop_width
crop_bottom = crop_top + crop_height
crop_4_tuple = (crop_left, crop_top, crop_right, crop_bottom)

crop = True
remove_old_files = False




def get_absolute_path_of_directories_and_files_in_rootpath(rootpath):
    # brrowed from: https://stackoverflow.com/questions/120656/directory-tree-listing-in-python?noredirect=1&lq=1
    directories_path, files_path = [], []

    for dirname, dirnames, filenames in os.walk(rootpath_for_conversion):
        
        for subdirname in dirnames:
            directories_path.append(os.path.join(dirname, subdirname))
        
        for filename in filenames:
            files_path.append(os.path.join(dirname, filename))

    return directories_path, files_path



if crop == True:

    print(f'\nBeginning file crop in rootpath {rootpath_for_conversion}.')
    print(f'Files with extension {current_extension} will be cropped to size (left={crop_left}, top={crop_top}, right={crop_right}, bottom={crop_bottom}).')
    if not remove_old_files: not_string = 'NOT '
    else: not_string = ''
    print(f'Old files will ' + not_string + 'be deleted!')
    answer = input('Continue? (Y/N): ')

    if answer.lower() in ['y', 'yes']:

        _, file_paths = get_absolute_path_of_directories_and_files_in_rootpath(rootpath_for_conversion)

        for file_path in file_paths:

            image_path, image_extension = os.path.splitext(file_path)

            if image_extension == current_extension:

                image = Image.open(file_path)
                cropped_image = image.crop(crop_4_tuple)
                cropped_image.save(image_path + "_cropped" + image_extension)
                image.close() 
                  
                print(f'CREATED: {image_path + "_cropped" + image_extension} was created (cropped).')
                
                if remove_old_files:
                    os.remove(file_path)
                    print(f'DELETED: {file_path} was deleted.')
            else: 
                print(f'UNCHANGED: {file_path} was unchanged.')

    elif answer.lower() in ['n', 'no']:
        print('Procedure aborted.')
    else:
        print("Procedure aborted due to bad user input, please answer 'Y' or 'N' next time.")