import glob
import numpy as np
import cv2 as cv

class Image:
    img = None
    name = ''

    def __init__(self, name):
        self.name = name[7:]  # Adjusted to remove directory prefix
        self.img = cv.imread(name)

def save_my_img(frame_count, img):
    if img is not None:
        path = 'C:/CS136-TermProject-CoralBabies-main/src/segmentation/Mean_Shift'  # Change to your directory
        name = f'/{frame_count}_mean_shift.png'
        print(f"Saving image to: {path + name}")
        cv.imwrite(path + name, img)
    else:
        print("No image to save!")

def mean_shift_segmentation(image):
    # Mean Shift Filtering
    spatial_radius = 20  # Spatial window radius
    color_radius = 30    # Color window radius
    max_level = 1        # Level of pyramid for Mean Shift

    # Apply Mean Shift Filtering
    result = cv.pyrMeanShiftFiltering(image.img, spatial_radius, color_radius, maxLevel=max_level)

    return result

# Main processing function
def process_images():
    images = [Image(file) for file in glob.glob("images/*.JPG")]  # Load images from the directory

    for image in images:
        result = mean_shift_segmentation(image)  # Perform Mean Shift segmentation
        save_my_img(image.name, result)  # Save the segmented result

    print("Process complete!")

if __name__ == "__main__":
    process_images()  # Run the image processing function