import glob
import os
import numpy as np
import cv2 as cv
from src.utils import utils

IMAGES_PATH = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\images'
SAVE_DIR = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\src\segmentation\Mean_Shift'

class Image:
    img = None
    name = ''

    def __init__(self, filepath):
        self.name, _ = os.path.splitext(os.path.basename(filepath))
        self.img = cv.imread(filepath)
        if self.img is None:
            print(f"Failed to load image: {filepath}")

def save_img(frame_name, img):
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)  # Ensure save directory exists

    if img is not None:
        save_path = os.path.join(SAVE_DIR, f"{frame_name}_mean_shift.jpg")
        print(f"Saving image: {frame_name}_mean_shift.jpg\n")
        cv.imwrite(save_path, img)
    else:
        print("No image to save!\n")

def mean_shift_segmentation(image: Image):
    print("Applying Mean Shift segmentation ...")

    # Convert the image to a feature space by blurring it slightly
    blurred = cv.pyrMeanShiftFiltering(image.img, sp=20, sr=40)
    
    return blurred


def mean_shift_segmentation_not_obj(img: np.ndarray):
    print("Applying Mean Shift segmentation ...")

    # Convert the image to a feature space by blurring it slightly
    blurred = cv.pyrMeanShiftFiltering(img, sp=20, sr=40)

    return blurred

# Main processing function
def process_images():
    Images = glob.glob(os.path.join(IMAGES_PATH, "*.JPG"))  # Load images from the directory

    if Images:
        print(f"Found {len(Images)} images. Starting processing...\n")
        
        for i, filepath in enumerate(Images, start=1):
            image = Image(filepath)
            print(f"Processing image {i}/{len(Images)}")
            result = mean_shift_segmentation(image)
            if result is not None:
                save_img(image.name, result)
    else:
        print("No images found in the specified directory!\n")

    print("Processing complete!")

def to_binary_mean_shift(dataset, save_path):
    for name, img in dataset.items():
        ret, binary_image = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # convert to binary
        img = cv.cvtColor(binary_image, cv.COLOR_GRAY2BGR) # Convert back to 3-channel
        img = mean_shift_segmentation_not_obj(img)
        cv.imwrite(f'{save_path}/{name}', img)

    return dataset


if __name__ == "__main__":
    #process_images()

    dataset_he = utils.get_imgs_from_src('../../contrast/histogram_equalization', 0)
    dataset_clahe = utils.get_imgs_from_src('../../contrast/clahe', 0)
    dataset_tahe = utils.get_imgs_from_src('../../contrast/tahe', 0)

    #dataset_he = to_binary_mean_shift(dataset_he, './binary_he')

    #dataset_clahe = to_binary_mean_shift(dataset_clahe, './binary_clahe')

    dataset_tahe = to_binary_mean_shift(dataset_tahe, './binary_tahe')

