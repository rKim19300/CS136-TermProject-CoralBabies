"""
    Contains useful functions can constants to save and load data
    into different files.

    @Author Reece Kim
"""

import os
import cv2
import numpy as np


# Spawn sizes (in pixels)

MAX_DIMS_TIMEPOINT0 = (110, 125) # Minor and major axes
MAX_DIMS_TIMEPOINT1 = (170, 215) # Minor and major axes

MIN_DIMS_TIMEPOINT0 = (50, 60) # Minor and major axes
MIN_DIMS_TIMEPOINT1 = (70, 85) # Minor and major axes

MAX_AREA_TIMEPOINT0 = 10800
MAX_AREA_TIMEPOINT1 = 28706

MIN_AREA_TIMEPOINT0 = 2356
MIN_AREA_TIMEPOINT1 = 4674

# Directory constant
ROOT_DIR = os.path.dirname(os.path.abspath(''))

# Just use the one that uses your own relative path
@DeprecationWarning
def get_dataset(cv2_enum: int) -> dict[str, np.ndarray]:
    """
    cv2_enum: The kind of images you want, (e.g. cv2.IMREAD_GRAYSCALE) for
              gray-scale images.

    :return: A dictionary of the sample images { <filename> : <numpy img array> }
    """
    dataset_names = os.listdir(os.path.join(ROOT_DIR, "dataset"))
    imgs = []
    for sample_name in dataset_names:
        imgs.append(cv2.imread(os.path.join(ROOT_DIR, f"dataset/{sample_name}"), cv2_enum))

    return dict(zip(dataset_names, imgs))

# Just use the one that uses your own relative path
@DeprecationWarning
def get_dataset_labeled(cv2_enum: int) -> dict[str, np.ndarray]:
    """
    cv2_enum: The kind of images you want, (e.g. cv2.IMREAD_GRAYSCALE) for
              gray-scale images.

    :return: A dictionary of the manually labled  sample images { <filename> : <numpy img array> }
    """
    dataset_names = os.listdir(os.path.join(ROOT_DIR, "labeled_data"))
    imgs = []
    for sample_name in dataset_names:
        imgs.append(cv2.imread(os.path.join(ROOT_DIR, f"labeled_data/{sample_name}"), cv2_enum))

    return dict(zip(dataset_names, imgs))

def get_imgs_from_src(dir_path: str, cv2_enum: int) -> dict[str, np.ndarray]:
    """
    Gets all imgs from a file that are in the directory path.

    dir_name: The name of the directory relative to your cwd

    cv2_enum: The kind of images you want, (e.g. cv2.IMREAD_GRAYSCALE) for
              gray-scale images.

    :return: A dictionary of the manually labled  sample images { <filename> : <numpy img array> }
    """

    valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".svg", ".ppm", ".pgm", ".pbm"]
    filenames = os.listdir(os.path.join(os.getcwd(), dir_path))

    imgs = []

    for filename in filenames:
        file_path = os.path.join(os.getcwd(), f"{dir_path}/{filename}")
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in valid_extensions:
            try:
                imgs.append(cv2.imread(file_path, cv2_enum))
            except Exception as e:
                print(f"Error opening {filename}: {e}")

    return dict(zip(filenames, imgs))

def save_imgs_to_src_file(dir_path: str, img_map: dict[str, np.ndarray]):
    """
    Save all images in the dict to a file relative to your current path

    dir_name: The name of the directory

    img_map: A dict with { <filename> : <numpy img array> }

    :return: A dictionary of the manually labled  sample images { <filename> : <numpy img array> }
    """

    path = os.path.join(os.getcwd(), dir_path)

    # If the directory does not exist, make it
    if not os.path.exists(path):
        os.makedirs(path)

    for filename, img in img_map.items():
        cv2.imwrite(f"{path}/{filename}", img)


def create_hstacks(dicts: list[dict[str, np.ndarray]], name_append: str) -> dict[str, np.ndarray]:
    """
    Creates hstacks from the dictionaries passed in as a list. These hstacks are used to
    compare the images side-by-side.

    :param dicts:        The dictionaries of images that will be passed in
    :param name_append:  The string that will be appended to the name of each hstack
                         in the output. This will be appended to the names contained in the
                         first dictionary of the list.
    :return:             A dictionary with the names of the images along with
    """

    # Initialize the result dict
    result = dict()

    # loop through the dicts and add each of them to the hstack
    for i in range(0, len(dicts[0])):
        img_list = []               # Initialize the list of images that will be in the stack

        # Populate img_list
        for img_dict in dicts:

            if len(img_dict) == 0:
                continue

            # pop current key-value from each dictionary
            key = next(iter(img_dict))
            value = img_dict.pop(key)
            img_list.append((key, value)) # Store as a tuple

        # Adjust the heights of each img and connect each other to one another in the hstack
        target_height = None

        ''' Add to hstack for comparison of photos'''
        # Find the height and width to resize the images for the hstack
        target_img = img_list[0][1]
        target_height = target_img.shape[0]
        new_width = int(target_img.shape[1] * (target_height / target_img.shape[0]))

        # Convert all images to 3 channels if they are grayscale
        for j in range(len(img_list)):
            img = img_list[j][1]
            if len(img.shape) == 2:  # Grayscale image (2D)
                img_list[j] = (img_list[j][0], cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))  # Convert to 3 channels

        # Iterate through the img list to resize and then append to hstack
        hstack = target_img  # Initialize the hstack with the 1st img
        for j in range(1, len(img_list)):

            resized_img = cv2.resize(img_list[j][1],
                                     (new_width, target_height), interpolation=cv2.INTER_AREA)

            # Stack imgs horizontally
            hstack = np.hstack((hstack, resized_img))

        # Add the stack to the result dict
        split_name = os.path.splitext(img_list[0][0])
        result = result | { f"{split_name[0]}{name_append}{split_name[1]}" : hstack }

    return result




