import numpy as np
import cv2


def luminosity(input_image):
    for x in range(len(input_image)):
        for y in range(len(input_image[x])):
            r = input_image[x][y][0]
            g = input_image[x][y][1]
            b = input_image[x][y][2]
            input_image[x][y] = 0.21 * r + 0.72 * g + 0.07 * b
    return input_image


def rgb2grays(input_image):
    # converts an RGB into grayscale by using 4 different methods

    # ligtness method

    # average method
    for x in range(input_image.shape[0]):
        for y in range(input_image.shape[1]):
            input_image[x][y] = np.sum(input_image[x][y]) / 3
    # print(new_image.shape, input_image.shape)
    print(input_image)
    return input_image

    # luminosity method

    # built-in opencv function 

    return luminosity(input_image)


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
