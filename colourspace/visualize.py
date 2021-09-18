import matplotlib.pyplot as plt
import numpy as np
import cv2


def visualize(input_image):
    # Fill in this function. Remember to remove the pass command
    
    if input_image.ndim == 2:
        plt.figure()
        plt.imshow(input_image, cmap='gray', vmin=0, vmax=255)
        plt.show()

    else:
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
