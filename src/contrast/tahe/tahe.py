import cv2
from src.utils import utils
import numpy as np
from src.connected_components import connected_components as cc
import os


if __name__ == '__main__':
    """
        The code used to generate the tahe images
    """

    # Load dataset
    dataset = utils.get_imgs_from_src('../../../dataset', cv2.IMREAD_GRAYSCALE)

    # Load the component data for each
    print("\nFinding the connected components in each colony map . . .\n")
    components = cc.get_colony_components('../../connected_components/marked_colony_map')

    # Find apply histogram equalization to each individual colony
    tahe_imgs = dict()
    tahe_imgs_no_noise = dict()
    for name, img in dataset.items():
        label_map, pixel_locations = components[name]  # The map and samples should have corresponding names

        # Apply histogram equalization to each component in the image
        # pixels hold a 2D np.ndarray in which the column has two values [row, col]
        for label, pixels in pixel_locations.items():
            # Extract the pixel intensities from the image
            pixel_intensities = img[pixels[:, 0], pixels[:, 1]]

            # compute the histogram for these specific intensities
            hist, bins = np.histogram(pixel_intensities, bins=256, range=[0, 256])

            # Find and normalize the cumulative distribution function
            cdf = hist.cumsum()

            # Mask and normalize the cdf
            cdf_m = np.ma.masked_equal(cdf, 0)  # Mask cdf where it is 0
            cdf_m = ((cdf_m - cdf_m.min()) * 255) / (cdf_m.max() - cdf_m.min())  # Normalize between 0 to 255
            cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # Filled masked values with 0

            # Apply equalized values to the pixel values of the component
            equalized_values = cdf[pixel_intensities]

            # Update the original image, but only for the current connected component
            img[pixels[:, 0], pixels[:, 1]] = equalized_values

        # Make two versions of the image, the 2nd being with the non-colonies blackout out
        img_no_noise = np.zeros_like(img)
        img_no_noise[label_map != 0] = img[label_map != 0]

        # Add images to their respective dicts
        tahe_imgs[name] = img
        tahe_imgs_no_noise[name] = img_no_noise

    # Save the new images to their respective files
    utils.save_imgs_to_src_file('./', tahe_imgs)
    utils.save_imgs_to_src_file('./nonoise', tahe_imgs_no_noise)





