"""
    Contains useful functions can constants to save and load data
    into different files. Note that this doesn't seem to work in a
    jupyter notebook.

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

def get_imgs_from_src(dir_path: str, cv2_enum: int) -> dict:
    """
    Gets all imgs from a file that is in src. Make sure that the dir_path does not
    start with "/", "./", or "../".

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

def save_imgs_to_src_file(dir_path: str, img_map: dict):
    """
    Save all images in the dict in a file in src. Make sure that the dir_path in src does not you
    choose does not start with "/", "./", or "../".

    dir_name: The name of the directory with src as the root

    img_map: A dict with { <filename> : <numpy img array> }

    :return: A dictionary of the manually labled  sample images { <filename> : <numpy img array> }
    """

    path = os.path.join(ROOT_DIR, f"src/{dir_path}")

    # If the directory does not exist, make it
    if not os.path.exists(path):
        os.makedirs(path)

    for filename, img in img_map.items():
        cv2.imwrite(f"{path}/{filename}", img)


def resize_and_pad(image, target_height, target_width):
    """
    Resizes an image to match the target height while preserving its aspect ratio.
    Adds padding to ensure the final image matches the target width.
    """
    original_height, original_width = image.shape[:2]
    aspect_ratio = original_width / original_height
    new_width = int(target_height * aspect_ratio)

    # Resize the image to maintain aspect ratio
    resized_image = cv2.resize(image, (new_width, target_height), interpolation=cv2.INTER_AREA)

    # Ensure target_width is sufficient
    if new_width > target_width:
        raise ValueError(f"Target width {target_width} is smaller than the resized width {new_width}. Increase the target width.")

    # Add padding to match target width
    delta_width = target_width - new_width
    left = delta_width // 2
    right = delta_width - left
    padded_image = cv2.copyMakeBorder(resized_image, 0, 0, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    return padded_image


