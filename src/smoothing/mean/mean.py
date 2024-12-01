import glob
import os
import cv2 as cv

class Image:
    img = None
    name = ''

    def __init__(self,name):
        self.name = name[7:]
        self.img = cv.imread(name)

images = [Image(file) for file in glob.glob("images/*.JPG")]

def save_my_img(frame_count, img):
    path = 'C:\Projects\CS136-TermProject-CoralBabies\mean'
    frame_count = frame_count[:-4]
    name = f'\{frame_count}'
    write = (path + name + "-mean.JPG")
    print(write)
    cv.imwrite(write, img)


for image in images:
    img = cv.blur(image.img, (3, 3))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    save_my_img(image.name, gray)

print("Process complete!")