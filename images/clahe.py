"""
    Applies CLAHE (Contrast Limited Adaptive Histogram Equalization) to the samples.
    CLAHE divides the image into multiple tiles and them equalizes the histogram within
    each of those tiles. If any pixels are above a contrast limit, they are clipped and
    distributed uniformly to other bins before applying equalization.

    NOTE: We can decide if we want to tune its parameters later

    @Author Reece Kim
"""

import os
from src.utils import utils
import cv2

def apply_clahe_grey():
    """
        Applies clache to both color and grey-scaled versions
    """

    # Load the dataset in color and gray
    dataset_color = utils.get_imgs_from_src('../../../dataset', cv2.IMREAD_COLOR)
    dataset_gray = utils.get_imgs_from_src('../../../dataset', cv2.IMREAD_GRAYSCALE)

    # Apply clahe to all
    clahe = cv2.createCLAHE() # Defaults: cliplimit = 40, tileGridSize = (8, 8)
    dataset_clahe = dict()
    for name, sample in dataset_gray.items():
        split_name = os.path.splitext(name)
        dataset_clahe[f'{split_name[0]}_clahe_cl40_tgs8x8{split_name[1]}'] = clahe.apply(sample)

    # create hstacks for comparison
    dataset_he = utils.get_imgs_from_src('../histogram_equalization', cv2.IMREAD_COLOR)
    dataset_labeled = utils.get_imgs_from_src('../../../labeled_data', cv2.IMREAD_COLOR)

    # hstacks [original, gray-scale, hist equal, clahe, labeled]
    compare = utils.create_hstacks([dataset_color, dataset_gray, dataset_he, dataset_clahe, dataset_labeled],
                                   '_clahe_cl40_tgs8x8_compare')

    # Save the images
    utils.save_imgs_to_src_file('./', dataset_clahe)
    utils.save_imgs_to_src_file('./hstacks', compare)


if __name__ == '__main__':
    apply_clahe_grey()
