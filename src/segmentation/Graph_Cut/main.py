import glob
import os
import numpy as np
import cv2 as cv

IMAGES_PATH = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\images'
SAVE_DIR    = r'C:\Users\az1do\Downloads\Compressed\CS136-TermProject-CoralBabies-main\CS136-TermProject-CoralBabies-main\src\segmentation\Graph_Cut'

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
        save_path = os.path.join(SAVE_DIR, f"{frame_name}_graph_cut.jpg")
        print(f"Saving image: {frame_name}_graph_cut.jpg\n")
        cv.imwrite(save_path, img)
    else:
        print("No image to save!\n")

def graph_cut_segmentation(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)

    # Apply Gaussian smoothing to reduce noise
    smoothed = cv.GaussianBlur(gray, (5, 5), 0)

    # Convert the grayscale smoothed image back to 3 channels (to match the expected input for grabCut)
    smoothed_colored = cv.cvtColor(smoothed, cv.COLOR_GRAY2BGR)

    # Create a mask for the initial segmentation (just an example, can be customized)
    mask = np.zeros(gray.shape, dtype=np.uint8)

    # Create GraphCut instance using OpenCV's GrabCut
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    
    # Define the rectangle for initial background/foreground segmentation
    rect = (10, 10, gray.shape[1]-10, gray.shape[0]-10)
    print("Grap cut is being applied ...")
    # Apply GrabCut segmentation algorithm
    cv.grabCut(smoothed_colored, mask, rect, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_RECT)

    # Modify the mask: 0=background, 2=probable background, 1=foreground, 3=probable foreground
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the image to get the segmented result
    result = image.img * mask2[:, :, np.newaxis]

    return result

# Main processing function
def process_images():
    
    Images = glob.glob(os.path.join(IMAGES_PATH, "*.JPG"))  # Load images from the directory

    if Images:
        print(f"Found {len(Images)} images. Starting processing...\n")
        
        for i, filepath in enumerate(Images, start=1):
            
            image = Image(filepath)
            print(f"Processing image {i}/{len(Images)}")
            result = graph_cut_segmentation(image)
            if result is not None:
                save_img(image.name, result)
    else:
        print("No images found in the specified directory!\n")

    print("Processing complete!")

if __name__ == "__main__":
    process_images()
