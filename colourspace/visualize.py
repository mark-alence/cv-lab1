import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cv2


def visualize(input_image, normalize=False):
    # Fill in this function. Remember to remove the pass command
    
    if input_image.ndim == 2:
        plt.figure()
        plt.imshow(input_image, cmap='gray', vmin=0, vmax=255)
        plt.show()

    else:
        if normalize:
            print('normalized')
            input_image = cv2.normalize(input_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        fig = plt.figure()  # new figure to plot
        sub1 = fig.add_subplot(2, 1, 1)
        sub1.set_title('Image')
        plt.imshow(input_image)

        # plt.figure()  # new figure to plot
        sub2 = fig.add_subplot(2, 3, 4)
        sub2.imshow(input_image[:, :, 0])  # Red
        sub2.set_title('Channel 1')
        #
        sub3 = fig.add_subplot(2, 3, 5)
        sub3.imshow(input_image[:, :, 1])  # Green
        sub3.set_title('Channel 2')
        #
        sub4 = fig.add_subplot(2, 3, 6)
        sub4.imshow(input_image[:, :, 2])  # Blue
        sub4.set_title('Channel 3')

        plt.show()

def visualize_gray(img_1, img_2, img_3, img_4):
    fig, axes = plt.subplots(2,2)

    #lightness
    axes[0,0].imshow(img_1, cmap='gray', vmin=0, vmax=255)
    axes[0,0].set_title('lightness')

    #average
    axes[0,1].imshow(img_2, cmap='gray', vmin=0, vmax=255)
    axes[0,1].set_title('average')

    #luminosity
    axes[1,0].imshow(img_3, cmap='gray', vmin=0, vmax=255)
    axes[1,0].set_title('luminosity')
    #opencv
    axes[1,1].imshow(img_4, cmap='gray', vmin=0, vmax=255)
    axes[1,1].set_title('opencv')
    plt.show()
