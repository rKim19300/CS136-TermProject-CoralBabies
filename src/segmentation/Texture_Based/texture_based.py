import glob
import os
import numpy as np
import cv2 as cv
from skimage.filters import gabor

# Directories for input images and saving results
IMAGES_PATH = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\images'
SAVE_DIR = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\src\segmentation\Texture_Based'

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
        save_path = os.path.join(SAVE_DIR, f"{frame_name}_texture_based.jpg")
        print(f"Saving image: {frame_name}_texture_based.jpg\n")
        cv.imwrite(save_path, img)
    else:
        print("No image to save!\n")

def texture_based_segmentation(image):
    print("Applying Texture-Based Segmentation ...")
    
    # Convert the image to grayscale for texture processing
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)

    # Define Gabor filter parameters
    frequencies = [0.1, 0.2, 0.3]  # Example frequencies
    thetas = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Directions
    
    # Initialize an empty array to store the texture responses
    texture_features = np.zeros_like(gray, dtype=np.float32)

    # Apply Gabor filters to extract texture information
    for frequency in frequencies:
        for theta in thetas:
            filtered_real, _ = gabor(gray, frequency=frequency, theta=theta)
            texture_features += np.abs(filtered_real)  # Combine filter responses

    # Normalize texture features to 0-255 range
    texture_features = cv.normalize(texture_features, None, 0, 255, cv.NORM_MINMAX).astype(np.uint8)

    # Thresholding for segmentation (Otsu's method)
    _, segmented_image = cv.threshold(texture_features, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return segmented_image

def process_images():
    Images = glob.glob(os.path.join(IMAGES_PATH, "*.JPG"))  # Load images from the directory

    if Images:
        print(f"Found {len(Images)} images. Starting processing...\n")
        
        for i, filepath in enumerate(Images, start=1):
            image = Image(filepath)
            if image.img is not None:
                print(f"Processing image {i}/{len(Images)}: {image.name}")
                result = texture_based_segmentation(image)
                if result is not None:
                    save_img(image.name, result)
            else:
                print(f"Skipping image {i}/{len(Images)} due to load error.")
    else:
        print("No images found in the specified directory!\n")

    print("Processing complete!")

if __name__ == "__main__":
    process_images()