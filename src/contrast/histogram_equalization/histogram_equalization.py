from utils import utils
import numpy as np
import cv2


if __name__ == '__main__':
    dataset = utils.get_imgs_from_src('', cv2.IMREAD_COLOR)

    for name, img in dataset.items():
        cv2.imshow(name, img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()