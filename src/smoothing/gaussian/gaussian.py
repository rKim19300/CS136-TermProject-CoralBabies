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
    path = 'C:\Projects\CS136-TermProject-CoralBabies\gaussian'
    name = f'\{frame_count}'
    print(path + name)
    cv.imwrite(path + name, img)

for image in images:
    img = cv.GaussianBlur(image.img, (3, 3), 0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    save_my_img(image.name, gray)

print("Process complete!")