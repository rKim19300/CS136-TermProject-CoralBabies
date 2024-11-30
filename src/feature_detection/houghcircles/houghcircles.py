import glob
import os
import numpy as np
import cv2 as cv

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

print("Process complete!")