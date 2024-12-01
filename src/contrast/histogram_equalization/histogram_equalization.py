from src.utils import utils
import numpy as np
import os
import cv2


if __name__ == '__main__':
    dataset = utils.get_dataset(cv2.IMREAD_COLOR)
    dataset_labeled = utils.get_dataset_labeled(cv2.IMREAD_COLOR)
    equalized = dict()
    stacked_compare = dict()

    for name, img in dataset.items():

        img_stack = img
        target_height = None

        # Equalize the image
        split = os.path.splitext(name)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equalized_img = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        equalized[f"{split[0]}_equalized{split[1]}"] = cv2.equalizeHist(equalized_img)

        ''' Add to hstack for comparison of photos'''
        # Find the height and width to resize the images for the hstack
        target_height = img.shape[0]
        new_width = int(equalized_img.shape[1] * (target_height / equalized_img.shape[0]))
        labeled_img = dataset_labeled[f"{split[0]}_labeled.png"]
        labeled_img = cv2.resize(labeled_img,
                                 (new_width, target_height), interpolation=cv2.INTER_AREA)
        gray_img = cv2.resize(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR),
                              (new_width, target_height), interpolation=cv2.INTER_AREA)
        equalized_img = cv2.resize(cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR),
                                 (new_width, target_height), interpolation=cv2.INTER_AREA)

        # Stack imgs horizontally
        img_stack = np.hstack((img_stack, gray_img))
        img_stack = np.hstack((img_stack, equalized_img))
        img_stack = np.hstack((img_stack, labeled_img))

        # Save to compare
        stacked_compare[f"{split[0]}_equalized_compare{split[1]}"] = img_stack

    #utils.save_imgs_to_src_file("contrast/histogram_equalization", equalized)
    utils.save_imgs_to_src_file("contrast/histogram_equalization/hstack", stacked_compare)