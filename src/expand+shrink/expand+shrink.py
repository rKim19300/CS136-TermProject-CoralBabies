"""
    This file is supposed to apply expand and shrink to the HE canny images, which is a
    preprocessing step to find the colonies as connected components

    @Author Reece Kim
"""

import cv2
from src.utils import utils
import numpy as np


def expand_and_shrink():

    # load the HE-canny samples
    he_canny = utils.get_imgs_from_src('../edgedetection/canny/hist_equ', 0)

    # expand, shrink, shrink, expand
    kernel = np.ones((3, 3), np.uint8)
    for name, img in he_canny.items():
        #img = cv2.erode(img, kernel, iterations=1)
        img = cv2.dilate(img, kernel, iterations=1)
        he_canny[name] = img

    # save the images
    utils.save_imgs_to_src_file('./k3x3_e', he_canny)

if __name__ == '__main__':
    expand_and_shrink()

