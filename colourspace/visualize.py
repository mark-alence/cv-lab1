import matplotlib.pyplot as plt
import numpy as np
import cv2


def visualize(input_image):
    # Fill in this function. Remember to remove the pass command

    plt.figure()  # new figure to plot
    plt.imshow(input_image.astype(np.uint8))
    plt.show()

    plt.figure()  # new figure to plot
    plt.subplot(1, 3, 1)
    plt.imshow(input_image[:, :, 0].astype(np.uint8))  # Red
    #
    plt.subplot(1, 3, 2)
    plt.imshow(input_image[:, :, 1].astype(np.uint8))  # Green
    #
    plt.subplot(1, 3, 3)
    plt.imshow(input_image[:, :, 2].astype(np.uint8))  # Blue

    plt.show()
    return
