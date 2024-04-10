##=====================================================##
##        File: add-scalebar-to-SEM-images.py
##      Author: GOTTFRID OLSSON 
##     Created: 2024-04-10
##     Updated: 2024-04-10
##       About: Takes a rootpath and adds a scalebar to
##              all .tif images in that path.
##=====================================================##

from PIL import Image, ImageDraw, ImageFont
import os


# CHANGE THESE FOR YOUR CASE #
rootpath_for_conversion = 'C:\\MASTER-THESIS\\EXPERIMENTAL\\Data\\SEM\\SEM images (.tif)\\Exported-SEM-images_2024-04-08' # remember to write '\\' for every '\'
current_extension = '.tif' 

add_scalebar = False
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
    magnification_micrometer_in_scalebar_per_magnification = [(131, 100), (200, 100), (500, 50), (800, 50), (1000, 10), (1200, 10), (2000, 10), (3000, 5), (5000, 5), (10000, 1)] # (magnification, mu_per_scalebar) as tuple
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

            try:
                magnification_i = int(magnification_i)
            except:
                print(f"EXCEPTION: Couldn't find magnification for filepath {file_path}. Skipping this item.")
                continue

            px_in_scalebar, micrometer_in_scalebar = get_micrometers_per_scalebar_for_magnification(magnification_i)


            if image_extension == current_extension:

                # Open image
                image = Image.open(file_path)
                draw = ImageDraw.Draw(image) # as to be able to draw lines on the image

                # coordinates
                width, height = image.size #in px
                text_height_px_offset = 10 #not true text height in px, but the offset
                px_offset = 25
                bottom_px_offset = px_offset + text_height_px_offset # taking into account text we want to write below
                right_px_offset = px_offset
                xy_coordinates_scalebar = [(width-right_px_offset-px_in_scalebar, height-bottom_px_offset),
                                           (width-right_px_offset,                height-bottom_px_offset)] # line will be draw between these (x,y) coorindates; [(x,y), (x,y), ...]
                x_center_of_scalebar = width-right_px_offset-0.5*px_in_scalebar
                y_center_of_scalebar = height-bottom_px_offset
                text_x_center = x_center_of_scalebar
                text_y_center = y_center_of_scalebar+0.7*text_height_px_offset
                rectangle_offset = 3
                rectangle_offset_bottom = 8
                ad_hoc_offset = 1
                xy_coordinates_rectangle = [(width-right_px_offset-px_in_scalebar-rectangle_offset, height-bottom_px_offset-rectangle_offset-ad_hoc_offset),
                                           (width-right_px_offset+rectangle_offset,                height-rectangle_offset_bottom-ad_hoc_offset)]


                # draw white rectangle
                draw.rectangle(xy_coordinates_rectangle, fill='white')

                # draw scalebar
                draw.line(xy_coordinates_scalebar, fill='black', width=3)

                # add scalebar text
                scalebar_text = str(micrometer_in_scalebar) + " μm" # half-space before "mu", use arial bcs. CMU Serif resulted in wonky "mu"
                font = ImageFont.truetype('C:\\MASTER-THESIS\\EXPERIMENTAL\\Python-scripts\\fonts\\arial.TTF', size=19)
                draw.text((text_x_center, text_y_center), scalebar_text, fill=(0,0,0), anchor="mt", font=font) # this will draw text with Blackcolor and 16 size # anchor: https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html#text-anchors
                
                # save image with drawn objects on
                image.save(image_path + "_added-scalebar" + image_extension)
                print(f'CREATED: {image_path + "_added-scalebar" + image_extension} was created.')
                image.close() 
                  

                if remove_old_files:
                    os.remove(file_path)
                    print(f'DELETED: {file_path} was deleted.')
            else: 
                print(f'UNCHANGED: {file_path} was unchanged.')

    elif answer.lower() in ['n', 'no']:
        print('Procedure aborted.')
    else:
        print("Procedure aborted due to bad user input, please answer 'Y' or 'N' next time.")
    
else:
    print("Set 'add_scalebar' to True in order to run the program.")