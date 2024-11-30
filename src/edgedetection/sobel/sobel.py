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
    path = 'C:\Projects\CS136-TermProject-CoralBabies\sobel'
    name = f'\{frame_count}'
    print(path + name)
    cv.imwrite(path + name, img)

for image in images:
    img = cv.GaussianBlur(image.img, (3, 3), 0)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grad_x = cv.Sobel(gray, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    save_my_img(image.name, grad)

print("Process complete!")