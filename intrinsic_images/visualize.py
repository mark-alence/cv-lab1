import matplotlib.pyplot as plt
import numpy as np
import cv2


def visualize(original_img, albedo_img, shading_img, reconstructed_img):
    # Fill in this function. Remember to remove the pass command
    
    fig, axes = plt.subplots(2,2)
    axes[0,0].imshow(albedo_img.astype(np.uint8))
    axes[0,0].set_title('Albedo Image')

    axes[0,1].imshow(shading_img.astype(np.uint8))
    axes[0,1].set_title('Shading Image')

    axes[1,0].imshow(original_img.astype(np.uint8))
    axes[1,0].set_title('Original Image')

    axes[1,1].imshow(reconstructed_img.astype(np.uint8))
    axes[1,1].set_title('Reconstructed Image')

    plt.show()
