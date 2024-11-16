"""
    Contains useful functions can constants to save and load data
    into different files.

    @Author Reece Kim
"""

import os
import cv2

ROOT_DIR = os.path.dirname(os.path.abspath('../../'))

def get_dataset(cv2_enum: int) -> dict:
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


def get_dataset_labeled(cv2_enum: int) -> dict:
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

def get_imgs_from_src(dir_path: str, cv2_enum: int):
    """
    Gets all imgs from a file that is in src

    dir_name: The name of the directory with src as the root

    cv2_enum: The kind of images you want, (e.g. cv2.IMREAD_GRAYSCALE) for
              gray-scale images.

    :return: A dictionary of the manually labled  sample images { <filename> : <numpy img array> }
    """

    valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".svg", ".ppm", ".pgm", ".pbm"]
    filenames = os.listdir(os.path.join(ROOT_DIR, f"src/{dir_path}"))
    imgs = []

    for filename in filenames:
        file_path = os.path.join(ROOT_DIR, f"src/{dir_path}/{filename}")
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in valid_extensions:
            try:
                imgs.append(cv2.imread(file_path, cv2_enum))
            except Exception as e:
                print(f"Error opening {filename}: {e}")

    return dict(zip(filenames, imgs))





