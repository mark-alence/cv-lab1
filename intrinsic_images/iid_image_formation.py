import cv2
import numpy as np
from visualize import visualize


def reconstruct_image(img_albedo: np.ndarray, img_shading:  np.ndarray) -> np.ndarray:
    reconstructed_img = np.float32(((img_albedo/255)*(img_shading/255)*255))
    return reconstructed_img

def main():
    ball_albedo_img = cv2.imread('ball_albedo.png')[:, :, ::-1]
    ball_shading_img = cv2.imread('ball_shading.png')[:, :, ::-1]
    ball_original_img = cv2.imread('ball.png')[:, :, ::-1]

    ball_reconstructed_img = reconstruct_image(ball_albedo_img, ball_shading_img)
    # print(ball_reconstructed_img.shape)
    # visualize(ball_albedo_img)
    # visualize(ball_original_img)
    # visualize(ball_reconstructed_img)
    visualize(ball_original_img, ball_albedo_img, ball_shading_img, ball_reconstructed_img)

    reconstructed_bgr = cv2.cvtColor(ball_reconstructed_img, cv2.COLOR_RGB2BGR)
    # print(reconstructed_bgr.shape)
    cv2.imwrite('ball_reconstructed.png', reconstructed_bgr)

if __name__ == '__main__':
    main()