import glob
import numpy as np
import cv2 as cv

class Image:
    img = None
    name = ''

    def __init__(self, name):
        self.name = name[7:]
        self.img = cv.imread(name)

def save_my_img(frame_count, img):
    if img is not None:
        path = 'C:/CS136-TermProject-CoralBabies-main/CS136-TermProject-CoralBabies-main/src/segmentation/Graph_ Cut'  # Change to your directory
        name = f'/{frame_count}_graphcut.png'
        print(f"Saving image to: {path + name}")
        cv.imwrite(path + name, img)
    else:
        print("no image")


def graph_cut_segmentation(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)

    # Initialize mask for Graph Cut algorithm (0=background, 1=foreground, 2=unknown)
    mask = np.zeros(image.img.shape[:2], np.uint8)

    # Define the foreground and background models (these are just arrays used for the Graph Cut)
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangle that roughly contains the foreground
    rect = (50, 50, image.img.shape[1] - 50, image.img.shape[0] - 50)

    # Apply Graph Cut (grabCut function)
    cv.grabCut(image.img, mask, rect, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_RECT)

    # Modify mask to separate foreground from background
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1)  # 0 for background, 1 for foreground

    # Create the final segmented image (foreground)
    result = image.img * mask2[:, :, np.newaxis]

    return result

# Main processing function
def process_images():
    images = [Image(file) for file in glob.glob("images/*.JPG")]  # Load images from the directory

    for image in images:
        result = graph_cut_segmentation(image)  # Perform graph cut segmentation
        save_my_img(image.name, result)  # Save the segmented result

    print("Process complete!")

if __name__ == "__main__":
    process_images()  # Run the image processing function