import numpy as np
import cv2


def rgb2grays(input_image, alg='opencv'):
    # converts an RGB into grayscale by using 4 different methods

    # ligtness method
    if alg == 'lightness':
        height, width, _ = input_image.shape
        new_image = np.zeros((height, width))
        for x in range(height):
            for y in range(width):
                rgb_pixel = input_image[x][y]
                # print(rgb_pixel)
                new_image[x][y] = (np.max(rgb_pixel) + np.min(rgb_pixel))/2

    # average method
    if alg == 'average':
        pass

    # luminosity method
    if alg == 'luminosity':
        pass
    # built-in opencv function
    if alg == 'opencv':
        new_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    return new_image


def rgb2opponent(input_image):
    # converts an RGB image into opponent colour space
    new_image = np.zeros(input_image.shape)
    for x in range(len(input_image)):
        for y in range(len(input_image[x])):
            r = input_image[x][y][0]
            g = input_image[x][y][1]
            b = input_image[x][y][2]
            new_image[x][y][0] = (r - g) / np.sqrt(2)
            new_image[x][y][1] = (r + g - 2 * b) / np.sqrt(6)
            new_image[x][y][2] = (r + g + b) / np.sqrt(3)
    return new_image


def rgb2normedrgb(input_image):
    # converts an RGB image into normalized rgb colour space
    new_image = np.zeros(input_image.shape)
    for x in range(len(input_image)):
        for y in range(len(input_image[x])):
            r = input_image[x][y][0]
            g = input_image[x][y][1]
            b = input_image[x][y][2]
            z = r + g + b
            if z == 0:
                z = 1
            new_image[x][y][0] = r / z
            new_image[x][y][1] = g / z
            new_image[x][y][2] = b / z
    return new_image
