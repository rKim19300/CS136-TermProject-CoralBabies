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
    path = 'C:\Projects\CS136-TermProject-CoralBabies\houghlines'
    name = f'\{frame_count}'
    print(path + name)
    cv.imwrite(path + name, img)

for image in images:
    dst = cv.Canny(image.img, 50, 200, None, 3)

    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

    save_my_img(image.name, cdstP)

print("Process complete!")