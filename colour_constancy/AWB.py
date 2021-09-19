from PIL.Image import new
import numpy as np
import cv2
import matplotlib.pyplot as plt

def AWB(input_image):
    R_avg, G_avg, B_avg = 0, 0, 0
    for i in range(len(input_image)):
        R_avg += np.sum(input_image[i].T[0])
        G_avg += np.sum(input_image[i].T[1])
        B_avg += np.sum(input_image[i].T[2])
    R_avg /= (input_image.shape[0] * input_image.shape[1])
    G_avg /= (input_image.shape[0] * input_image.shape[1])
    B_avg /= (input_image.shape[0] * input_image.shape[1])

    new_image = [[0 for i in range(input_image.shape[1])] 
                for j in range(input_image.shape[0])]
    # print(np.array(new_image).shape, np.array(input_image).shape)
    for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            new_pixel = [input_image[i][j][0] / R_avg, input_image[i][j][1] / G_avg, 
                        input_image[i][j][2] / B_avg]
            new_image[i][j] = new_pixel

    new_image /= np.max(new_image)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(input_image)
    plt.subplot(1, 2, 2)
    plt.title('Color Constant Image')
    plt.imshow(new_image)
    plt.show()
    

if __name__ == '__main__':
    # Replace the image name with a valid image
    img_path = 'awb.jpg'
    # Read with opencv
    I = cv2.imread(img_path)
    # Convert from BGR to RGB
    # This is a shorthand.
    I = I[:, :, ::-1]
    plt.show()
    out_img = AWB(I)