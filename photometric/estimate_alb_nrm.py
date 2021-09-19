import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def estimate_alb_nrm(image_stack, scriptV, shadow_trick=False):
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

    for y in range(h):
        for x in range(w):
            i = image_stack[y][x]
            scriptI = np.diag(i)
            if shadow_trick:
                g = np.linalg.lstsq(scriptI @ scriptV, scriptI @ i, rcond=None)[0]
            else:
                g = np.linalg.lstsq(scriptV, i, rcond=None)[0]
            norm = np.linalg.norm(g)
            albedo[y][x] = norm
            if norm == 0:
                normal[y][x] = [0, 0, 0]
            else:
                normal[y][x] = g / norm

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


