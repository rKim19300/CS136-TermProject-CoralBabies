import glob
import os
import numpy as np
import cv2 as cv

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

def mean_shift_segmentation(image):
    print("Applying Mean Shift segmentation ...")
    src = image.img
    sp = 20  # Spatial window radius
    sr = 40  # Color window radius
    # Apply Mean Shift Segmentation
    segmented_image = cv.pyrMeanShiftFiltering(src, sp, sr)

    return segmented_image 

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

if __name__ == "__main__":
    process_images()
