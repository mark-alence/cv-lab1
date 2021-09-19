import numpy as np
import rgbConversions
from visualize import *
import cv2
import matplotlib.pyplot as plt


def ConvertColourSpace(input_image, colourspace):
    '''
    Converts an RGB image into a specified color space, visualizes the
    color channels and returns the image in its new color space.

    Colorspace options:
      opponent
      rgb -> for normalized RGB
      hsv
      ycbcr
      gray

    P.S: Do not forget the visualization part!
    '''

    # Convert the image into double precision for conversions
    input_image = input_image.astype(np.float32)

    if colourspace.lower() == 'opponent':
        # fill in the rgb2opponent function
        new_image = rgbConversions.rgb2opponent(input_image)

    elif colourspace.lower() == 'rgb':
        new_image = rgbConversions.rgb2normedrgb(input_image)

    elif colourspace.lower() == 'hsv':
        new_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2HSV)

    elif colourspace.lower() == 'ycrcb':
        new_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2YCrCb)

    elif colourspace.lower() == 'gray':
        lightness_image = rgbConversions.rgb2grays(input_image, alg='lightness')
        average_image = rgbConversions.rgb2grays(input_image, alg='average')
        luminosity_image = rgbConversions.rgb2grays(input_image, alg='luminosity')
        opencv_image = rgbConversions.rgb2grays(input_image, alg='opencv')
        visualize_gray(lightness_image, average_image, luminosity_image, opencv_image)

    else:
        print('Error: Unknown colorspace type [%s]...' % colourspace)
        new_image = input_image

    if not colourspace.lower() == 'gray':
        visualize(new_image, normalize=True)

    return new_image


if __name__ == '__main__':
    # Replace the image name with a valid image
    img_path = 'giannis.jpg'
    # Read with opencv
    I = cv2.imread(img_path)
    # Convert from BGR to RGB
    # This is a shorthand.
    I = I[:, :, ::-1]
    out_img = ConvertColourSpace(I, 'ycrcb')
