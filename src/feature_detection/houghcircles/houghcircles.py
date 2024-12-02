import glob
import os
import numpy as np
import cv2 as cv
from src.utils import utils

class Image:
    img = None
    name = ''

    def __init__(self,name):
        self.name = name[7:]
        self.img = cv.imread(name)

images = [Image(file) for file in glob.glob("images/*.JPG")]

def save_my_img(frame_count, img):
    path = 'C:\Projects\CS136-TermProject-CoralBabies\houghcircles'
    name = f'\{frame_count}'
    print(path + name)
    cv.imwrite(path + name, img)

for image in images:
    gray = cv.cvtColor(image.img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8, param1=50, param2=30, minRadius=1, maxRadius=30)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(image.img, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(image.img, center, radius, (255, 0, 255), 3)

    save_my_img(image.name, image.img)

# According to utils
MAX_RADIUS = 112 # Max diameter is 215
MIN_RADIUS = 20  # Min diameter is 50


def apply_hough_circles(dataset):
    new_dataset = dict()
    for name, img in dataset.items():
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        print('\nComputing circles . . .\n')
        circles = cv.HoughCircles(gray,
                                  cv.HOUGH_GRADIENT,
                                  dp=1,
                                  minDist=MIN_RADIUS * 2,
                                  param1=50, # Canny threshold
                                  param2=30, # Votes needed
                                  minRadius=MIN_RADIUS,
                                  maxRadius=MAX_RADIUS
                                  )
        split_name = os.path.splitext(name)
        new_dataset[f'{split_name[0]}_circles{split_name[1]}'] = draw_circles(circles, img)
    return new_dataset


def draw_circles(circles, img) -> np.ndarray:
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(img, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(img, center, radius, (255, 0, 255), 3)
    return img

print("Process complete!")


if __name__ == '__main__':

    # Load dataset
    #dataset_he = utils.get_imgs_from_src('../../contrast/histogram_equalization', cv.IMREAD_COLOR)
    #dataset_clahe = utils.get_imgs_from_src('../../contrast/clahe', cv.IMREAD_COLOR)
    #dataset_tahe = utils.get_imgs_from_src('../../contrast/tahe', cv.IMREAD_COLOR)
    dataset_tahe_nonoise = utils.get_imgs_from_src('../../contrast/tahe/nonoise', cv.IMREAD_COLOR)
    #dataset = utils.get_imgs_from_src('../../../dataset', cv.IMREAD_COLOR)
    #dataset_bms_tahe = utils.get_imgs_from_src('../../segmentation/Mean_Shift/binary_tahe', cv.IMREAD_COLOR)


    print('\nApplying hough to dataset he . . .\n')
    #dataset_he = apply_hough_circles(dataset_he)
    #utils.save_imgs_to_src_file('./equalized_tuned', dataset_he)

    print('\nApplying hough to dataset clahe . . .\n')
    #dataset_clahe = apply_hough_circles(dataset_clahe)
    #utils.save_imgs_to_src_file('./clahe_tuned', dataset_clahe)

    print('\nApplying hough to dataset tahe . . .\n')
    #dataset_tahe = apply_hough_circles(dataset_tahe)
    #utils.save_imgs_to_src_file('./tahe_tuned', dataset_tahe)

    print('\nApplying hough to dataset tahe nonoise . . .\n')
    dataset_tahe_nonoise = apply_hough_circles(dataset_tahe_nonoise)
    utils.save_imgs_to_src_file('./tahe_nonoise', dataset_tahe_nonoise)

    print('\nApplying hough to dataset control . . .\n')
    #dataset = apply_hough_circles(dataset)
    #utils.save_imgs_to_src_file('./control_tuned', dataset)

    print('\nApplying hough to dataset binary mean-shift tahe  . . .\n')
    #dataset_bms_tahe = apply_hough_circles(dataset_bms_tahe)
    #utils.save_imgs_to_src_file('./binary_ms_tahe', dataset_bms_tahe)
