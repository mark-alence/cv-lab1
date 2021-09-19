import cv2
import numpy as np
from iid_image_formation import reconstruct_image
from visualize import visualize

def get_true_color(albedo_img):
    for x in range(albedo_img.shape[0]):
        for y in range(albedo_img.shape[1]):
            if np.all(albedo_img[x][y]):
                return albedo_img[x][y]

def recolor_image(albedo_img):
    for x in range(albedo_img.shape[0]):
        for y in range(albedo_img.shape[1]):
            if np.all(albedo_img[x][y]):
                albedo_img[x][y] = [0, 255, 0]
    return albedo_img

def main():
    ball_albedo_img = cv2.cvtColor(cv2.imread('ball_albedo.png'), cv2.COLOR_BGR2RGB)
    ball_shading_img = cv2.cvtColor(cv2.imread('ball_shading.png'), cv2.COLOR_BGR2RGB)
    ball_original_img = cv2.cvtColor(cv2.imread('ball.png'), cv2.COLOR_BGR2RGB)

    true_color = get_true_color(ball_albedo_img)
    print(f"True color: {true_color}")
    albedo_recolored = recolor_image(ball_albedo_img)
    recolored_img = reconstruct_image(albedo_recolored, ball_shading_img)

    visualize(ball_original_img, albedo_recolored, ball_shading_img, recolored_img)

if __name__ == '__main__':
    main()