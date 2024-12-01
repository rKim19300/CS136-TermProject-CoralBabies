import glob
import numpy as np
import cv2 as cv
import os

IMAGES_PATH = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\images'
SAVE_DIR    = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\src\segmentation\Region_Based'

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
        save_path = os.path.join(SAVE_DIR, f"{frame_name}_region_based.jpg")
        print(f"Saving image: {frame_name}_region_based.jpg\n")
        cv.imwrite(save_path, img)
    else:
        print("No image to save!\n")

def region_based_segmentation(image):
    # Convert to grayscale
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Perform Otsu's thresholding
    _, thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Create a mask for segmentation
    mask = np.zeros_like(gray)

    # Fill detected regions in the mask
    for contour in contours:
        cv.drawContours(mask, [contour], -1, 255, thickness=cv.FILLED)

    # Apply the mask to the original image
    segmented = cv.bitwise_and(image.img, image.img, mask=mask)

    return segmented

# Main processing function
def process_images():
    
    Images = glob.glob(os.path.join(IMAGES_PATH, "*.JPG"))  # Load images from the directory

    if Images:
        print(f"Found {len(Images)} images. Starting processing...\n")
        
        for i, filepath in enumerate(Images, start=1):
            
            image = Image(filepath)
            print(f"Processing image {i}/{len(Images)}")
            result = region_based_segmentation(image)
            if result is not None:
                save_img(image.name, result)
    else:
        print("No images found in the specified directory!\n")

    print("Processing complete!")

if __name__ == "__main__":
    process_images()