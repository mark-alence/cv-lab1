import matplotlib.pyplot as plt
import numpy as np
import cv2


def visualize(input_image):

    plt.figure()  # new figure to plot
    plt.imshow(input_image.astype(np.uint8))
    plt.show()

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.imshow(input_image[:, :, 0].astype(np.uint8))
    plt.subplot(1, 3, 2)
    plt.imshow(input_image[:, :, 1].astype(np.uint8))
    plt.subplot(1, 3, 3)
    plt.imshow(input_image[:, :, 2].astype(np.uint8))

    plt.show()
    return
