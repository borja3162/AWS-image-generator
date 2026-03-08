from  PIL import Image
# import numpy as np







def _is_pixel_painted(i, j, spacing_param:int):
    """
    Given i,j indices it returns True if the pixel is going to be painted at the output image
    """
    check_1 =(i//4  +j//4) %spacing_param == 0
    check_2 = (i//(4+spacing_param) +j//(4+spacing_param) )% spacing_param == 0
    return check_1 or check_2


def _ensure_proper_color_value(value):

    if value > 255:
        value = 255
    if value < 0:
        value=0

    return value

def _get_pixel_color(i,j,spacing_param:int, color_value , color_default= (255,255,255)):
    """
    Gets a color for a given pixel (i,j).
    """
    if _is_pixel_painted(i, j, spacing_param):
        return color_value
    else:
        return color_default



def generate_image(output_path, width :int, height:int,
                   spacing_param:int,red_val, green_val, blue_val):

    """
    Generates an image on the output_path with dimensions (width, height) .
    (red_val, green_val, blue_val) represent an RGB color, and they should be values between 0 and 255.

    spacing_param is expected to be a positive integer: different values create different patterns on the images.
    """


    # management of parameters so they are in proper ranges
    if spacing_param < 1:
        spacing_param=1

    red_val = _ensure_proper_color_value(red_val)
    green_val = _ensure_proper_color_value(green_val)
    blue_val = _ensure_proper_color_value(blue_val)
    color_val_when_painted= (red_val, green_val, blue_val)



    # RBG array creation

    image = Image.new("RGB", (width, height))
    img_array = image.load()  # gives a pixel-access object


    for i in range(height):
        for j in range(width):
            img_array[i,j] = _get_pixel_color(i,j,spacing_param, color_val_when_painted)



    # Saving array as image

    image.save(output_path)
