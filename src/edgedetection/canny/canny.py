import glob
import os
import cv2 as cv
import numpy as np
from src.utils import utils
"""
class Image:
    img = None
    name = ''

    def __init__(self,name):
        self.name = name[7:]
        self.img = cv.imread(name)

images = [Image(file) for file in glob.glob("images/*.JPG")]

def save_my_img(frame_count, img):
    path = 'C:\Projects\CS136-TermProject-CoralBabies\canny'
    name = f'\{frame_count}'
    print(path + name)
    cv.imwrite(path + name, img)

for image in images:
    img = cv.GaussianBlur(image.img, (3, 3), 0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_blur = cv.blur(gray, (3, 3))
    detected_edges = cv.Canny(img_blur, 50, 150, 3)
    mask = detected_edges != 0
    dst = cv.cvtColor(image.img * (mask[:,:,None].astype(image.img.dtype)), cv.COLOR_BGR2GRAY)

    save_my_img(image.name, dst)

print("Process complete!")
"""

if __name__ == '__main__':

    # Get the equalized HE images
    dataset_he = utils.get_imgs_from_src('../../contrast/histogram_equalization', cv.COLOR_BGR2GRAY)
    inverted_canny = dict()

    for name, img in dataset_he.items():
        inverted_img = 255 - img # Invert the image
        blurred_img = cv.GaussianBlur(inverted_img, (3, 3), 0) # Apply Gaussian blur to the img
        blurred_img = cv.blur(blurred_img, (3, 3)) # Average blur
        detected_edges = cv.Canny(blurred_img, 50, 150, 3)

        # Use a mask on the original image
        mask = detected_edges != 0
        dst = inverted_img * mask.astype(img.dtype)
        inverted_canny[name] = dst

    # Store the result
    #utils.save_imgs_to_src_file('./equalized_inverted', inverted_canny)

    # Load the labeled and regular canny dataset
    #labeled_data = utils.get_imgs_from_src('../../../labeled_data', cv.IMREAD_COLOR)
    #canny = utils.get_imgs_from_src('./equalized', cv.IMREAD_COLOR)

    #compare = utils.create_hstacks([canny, inverted_canny, labeled_data], '_compare')
    #utils.save_imgs_to_src_file('./he_vs_invhe_vs_labeled', compare)







