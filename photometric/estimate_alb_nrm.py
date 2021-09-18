import os

import cv2
import numpy as np


def estimate_alb_nrm(image_stack, scriptV, shadow_trick=True):
    # COMPUTE_SURFACE_GRADIENT compute the gradient of the surface
    # INPUT:
    # image_stack : the images of the desired surface stacked up on the 3rd dimension
    # scriptV : matrix V (in the algorithm) of source and camera information
    # shadow_trick: (true/false) whether or not to use shadow trick in solving linear equations
    # OUTPUT:
    # albedo : the surface albedo
    # normal : the surface normal

    h, w, n = image_stack.shape

    # create arrays for 
    # albedo (1 channel)
    # normal (3 channels)
    albedo = np.zeros([h, w])
    normal = np.zeros([h, w, 3])

    i = image_stack.T

    for x in range(w):
        for y in range(h):
            scriptI = np.diag(i[x][y])


    for idx in range(len(i)):
        row = idx//w
        scriptI = np.diag(i[idx])
        g = np.linalg.inv(scriptV)@np.linalg.inv(scriptI)@scriptI@i
        albedo[row][idx - w*row] = np.linalg.norm(g)
        normal[row][idx - w*row] = g/np.linalg.norm(g)

    """
    ================
    Your code here
    ================
    for each point in the image array
        stack image values into a vector i
        construct the diagonal matrix scriptI
        solve scriptI * scriptV * g = scriptI * i to obtain g for this point
        albedo at this point is |g|
        normal at this point is g / |g|
    """

    return albedo, normal


if __name__ == '__main__':
    n = 5
    paths = os.listdir("photometrics_images/SphereGray5")
    directions = [path.split('_') for path in paths]
    images = [cv2.imread(f"photometrics_images/SphereGray5/{path}", cv2.IMREAD_GRAYSCALE) for path in paths]
    # image_stack = np.zeros([10, 10, n])
    image_stack = np.stack(images, axis=2)
    scriptV = np.zeros([n, 3])
    estimate_alb_nrm(image_stack, scriptV, shadow_trick=True)
