##=====================================================##
##        File: crop_images.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-08-16
##     Updated: 2023-08-16
##       About: Takes a rootpath and adds a scalebar to
##              all .tif images in that path.
##=====================================================##

from PIL import Image, ImageDraw, ImageFont
import os
import re #regular expression


# CHANGE THESE FOR YOUR CASE #
#rootpath_for_conversion = 'C:\\MASTER-THESIS\\EXPERIMENTAL\\Data\\SEM\\SEM images (.tif)\\Exported-SEM-images_2024-04-08' # remember to write '\\' for every '\'
rootpath_for_conversion = 'C:\\MASTER-THESIS\\EXPERIMENTAL\\Data\\SEM\\SEM images (.tif)\\Exported-SEM-images_2024-04-08\\SEM-02_20kV20nA' # remember to write '\\' for every '\'
current_extension = '.tif' 

add_scalebar = True
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


def micrometer_per_pixel(SEM_magnification):
    return 195 / (SEM_magnification + 6.6) #micrometer per pixel as function of magnification (times, e.g. 1000 or 5000) in the SEM (PHI 700 Scanning auger nanoprobe, in IMS at Chalmers)


def get_micrometers_per_scalebar_for_magnification(magnification):
    # e.g. 131X = magnification of 131 times
    magnification_micrometer_in_scalebar_per_magnification = [(131, 100), (500, 50), (1000, 10), (3000, 5), (5000, 5), (10000, 1)] # (magnification, mu_per_scalebar) as tuple
    magnifications = [tuple[0] for tuple in magnification_micrometer_in_scalebar_per_magnification]
    micrometer_in_scalebar_per_magnification = [tuple[1] for tuple in magnification_micrometer_in_scalebar_per_magnification]
    micrometer_in_scalebar = 0

    for i in range(len(magnifications)):
        if magnification == magnifications[i]:
            micrometer_in_scalebar = micrometer_in_scalebar_per_magnification[i]
            continue

    mu_per_px = micrometer_per_pixel(float(magnification))
    px_per_mu = 1/mu_per_px
    px_in_scalebar = int(px_per_mu * micrometer_in_scalebar)

    return px_in_scalebar, micrometer_in_scalebar


def find_magnification_X_from_string(string):
    # finds and returns the number '123456789' from example string:
    # "[...]_magnification-123456789X_[...]"" that is the string of the image
    # se partition: https://www.w3schools.com/python/ref_string_partition.asp
    part_after_magnification = string.partition('magnification-')[2] #returns string after 'magnification-'
    part_before_X = part_after_magnification.partition('X')[0] #returns string before 'X' in the already split string above

    return part_before_X 


if add_scalebar == True:

    print(f'\nStart adding scalebar in rootpath {rootpath_for_conversion}.')
    print(f'Files with extension {current_extension} will be given a scalebar based on their magnification.')
    if not remove_old_files: not_string = 'NOT '
    else: not_string = ''
    print(f'Old files will ' + not_string + 'be deleted!')
    answer = input('Continue? (Y/N): ')

    if answer.lower() in ['y', 'yes']:

        _, file_paths = get_absolute_path_of_directories_and_files_in_rootpath(rootpath_for_conversion)

        for file_path in file_paths:

            image_path, image_extension = os.path.splitext(file_path)

            # Get magnification from file_path
            magnification_i = find_magnification_X_from_string(image_path)
            print(magnification_i)
            magnification_i = int(magnification_i)
            px_in_scalebar, micrometer_in_scalebar = get_micrometers_per_scalebar_for_magnification(magnification_i)
            print(magnification_i, px_in_scalebar, micrometer_in_scalebar)

            if image_extension == current_extension:

                image = Image.open(file_path)
                width, height = image.size
                draw = ImageDraw.Draw(image) # as to be able to draw lines on the image

                # draw scalebar
                text_height_px_offset = 10 #not true text height in px, but the offset
                bottom_px_offset = 25 + text_height_px_offset # taking into account text we want to write below
                right_px_offset = 25
                xy_coordinates = [(width-right_px_offset-px_in_scalebar, height-bottom_px_offset),
                                  (width-right_px_offset,                height-bottom_px_offset)] # line will be draw between these (x,y) coorindates; [(x,y), (x,y), ...]
                draw.line(xy_coordinates, fill='black', width=3)
                
                x_center_of_scalebar = width-right_px_offset-0.5*px_in_scalebar
                y_center_of_scalebar = height-bottom_px_offset

                # add text x mu with CMU Serif font
                # TODO
                scalebar_text = str(micrometer_in_scalebar) + " μm"
                #font = ImageFont.truetype('C:\\Windows\\Fonts\\CMU Serif\\CMU Serif Roman.ttf', 20)
                draw.text((x_center_of_scalebar, y_center_of_scalebar-text_height_px_offset), scalebar_text, fill = (0,0,0))#, font=font) # this will draw text with Blackcolor and 16 size

                image.save(image_path + "_added-scalebar" + image_extension)
                image.close() 
                  
                print(f'CREATED: {image_path + "_added-scalebar" + image_extension} was created.')
                
                if remove_old_files:
                    os.remove(file_path)
                    print(f'DELETED: {file_path} was deleted.')
            else: 
                print(f'UNCHANGED: {file_path} was unchanged.')

    elif answer.lower() in ['n', 'no']:
        print('Procedure aborted.')
    else:
        print("Procedure aborted due to bad user input, please answer 'Y' or 'N' next time.")