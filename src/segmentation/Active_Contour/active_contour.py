import glob
import os
import numpy as np
from skimage.segmentation import active_contour
from skimage.filters import gaussian
from skimage.color import rgb2gray
import cv2 as cv


IMAGES_PATH = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\images'
SAVE_DIR    = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\src\segmentation\Active_Contour'

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
        save_path = os.path.join(SAVE_DIR, f"{frame_name}_active_contour.jpg")
        print(f"Saving image: {frame_name}_active_contour.jpg\n")
        cv.imwrite(save_path, img)
    else:
        print("No image to save!\n")

def active_contour_segmentation(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)

    # Apply Gaussian smoothing to reduce noise
    smoothed = cv.GaussianBlur(gray, (5, 5), 0)

    # Define an initial snake contour (a circle or ellipse within the image)
    s = np.linspace(0, 2 * np.pi, 400)
    x = gray.shape[1] // 2 + gray.shape[1] // 4 * np.cos(s)  # Horizontal center + radius
    y = gray.shape[0] // 2 + gray.shape[0] // 4 * np.sin(s)  # Vertical center + radius
    init = np.array([x, y]).T  # Initial snake coordinates
    print("Active contour is being applied ...")
    # Perform Active Contour Model. To make it faster gamma may be increased
    snake = active_contour(smoothed, init, alpha=0.015, beta=10, gamma=0.1)

    # Create a binary mask from the snake
    mask = np.zeros(gray.shape, dtype=np.uint8)
    snake_int = np.round(snake).astype(int)  # Convert to integer coordinates
    cv.fillPoly(mask, [snake_int], 1)  # Fill inside the snake

    # Create the segmented image by applying the mask
    result = image.img * mask[:, :, np.newaxis]

    return result

# Main processing function
def process_images():
    
    Images = glob.glob(os.path.join(IMAGES_PATH, "*.JPG"))  # Load images from the directory

    if Images:
        print(f"Found {len(Images)} images. Starting processing...\n")
        
        for i, filepath in enumerate(Images, start=1):
            
            image = Image(filepath)
            print(f"Processing image {i}/{len(Images)}")
            result = active_contour_segmentation(image)
            if result is not None:
                save_img(image.name, result)
    else:
        print("No images found in the specified directory!\n")

    print("Processing complete!")

if __name__ == "__main__":
    process_images()
