import cv2
import matplotlib.pyplot as plt
from src.utils import utils
import numpy as np
from enum import Enum


def generate_rgb_histograms(dataset: dict[str, np.ndarray], save_dir: str):
    """
        Excludes black pixels
    """
    colors = ('b', 'g', 'r')

    for name, img in dataset.items():
        mask = np.all(img > 0, axis=-1)  # Ensure all channels are greater than 0
        for i, color in enumerate(colors):
            hist = cv2.calcHist([img], [i], mask.astype(np.uint8) * 255, [256], [0, 256])
            plt.plot(hist, color=color, label=f'{color.upper()} Channel')  # Add label for each channel

        plt.xlabel('Intensity Value')
        plt.xticks(np.arange(0, 255, step=25))
        plt.ylabel('Pixel Count')
        plt.yticks(np.arange(0, 250000, step=10000))
        plt.title(f'{name} RGB Histogram')
        plt.legend()

        # Save the histogram plot as an image
        plt.savefig(f'{save_dir}/{name}_rgb_hist.png')

        # Clear the figure for the next image
        plt.clf()




def generate_hsi_histograms(dataset: dict[str, np.ndarray], save_dir: str):
    """
        Excludes black pixels
    """

    hsi_colors = ['m', 'c', 'y']
    hsi_names = ['Hue', 'Saturation', 'Intensity']
    for name, img in dataset.items():
        hsi_sample = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        fig, axes = plt.subplots(nrows=1, ncols=3, sharex=False, sharey=False)

        # Split into H, S, and v channels (v is similar to intensity)
        h, s, v = cv2.split(hsi_sample)

        mask_s = s > 0
        mask_v = v > 0

        hist_h = cv2.calcHist([hsi_sample], [0], None, [180], [0, 180])
        hist_s = cv2.calcHist([hsi_sample], [1], mask_s.astype(np.uint8), [255], [0, 255])
        hist_v = cv2.calcHist([hsi_sample], [2], mask_v.astype(np.uint8), [255], [0, 255])

        for i, hist in enumerate([hist_h, hist_s, hist_v]):
            axes[i].plot(hist, hsi_colors[i])

            axes[i].set_xlabel('Value')
            axes[i].set_xticks(np.arange(0, len(hist) - 1, step=50))
            axes[i].set_ylabel('Pixel Count')
            yrange = 2000000 if i == 0 else 200000
            ysteps = 100000 if i == 0 else 20000
            axes[i].set_yticks(np.arange(0, yrange, step=ysteps))
            axes[i].set_title(f'{hsi_names[i]} Hist')

        plt.savefig(f'{save_dir}/{name}_hsi_hist.png') # Save the histogram
        plt.clf() # Clear the pyplot


def generate_gray_histograms(dataset: dict[str, np.ndarray], save_dir: str):
    """
        Excludes black pixels
    """

    for name, img in dataset.items():
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = img_gray > 0
        hist = cv2.calcHist([img_gray], [0], mask.astype(np.uint8), [256], [0, 256])
        plt.plot(hist)

        plt.xlabel('Intensity Value')
        plt.xticks(np.arange(0, len(hist) - 1, step=25))
        plt.ylabel('Pixel Count')
        plt.yticks(np.arange(0, 140000, step=10000))
        plt.title(f'{name} Gray-scale Hist')

        plt.savefig(f'{save_dir}/{name}_gray_hist.png') # Save the histogram

        plt.clf() # Clear the pyplot

def generate_gray_hsi_rgb_hists():
    """
        Generates the histograms for the gray, hsi, and rgb control vs blackout histograms.
        Saves them to their respective files
    """
    # Get the base dataset
    dataset_base = utils.get_imgs_from_src('../../dataset', cv2.IMREAD_COLOR)
    for name, img in dataset_base.items(): # Change the dimensions to be of roughly blackout's
        dataset_base[name] = cv2.resize(img, (2500, 2500))

    # Get the dataset with the spawn blackened out
    dataset_blackout = utils.get_imgs_from_src('../../black_out_data', cv2.IMREAD_COLOR)

    # Make rgb, hsi, and grayscale histograms of both datasets
    dataset_names = ('control', 'blackout')
    for i, dataset in enumerate([dataset_base, dataset_blackout]):
        generate_gray_histograms(dataset, f'./gray/{dataset_names[i]}')
        generate_rgb_histograms(dataset, f'./rgb/{dataset_names[i]}')
        generate_hsi_histograms(dataset,f'./hsi/{dataset_names[i]}')


if __name__ ==  '__main__':

    generate_gray_hsi_rgb_hists()

    # Merge the histograms control and blackout histograms to compare
    gray_control = utils.get_imgs_from_src('./gray/control', cv2.IMREAD_COLOR)
    gray_blackout = utils.get_imgs_from_src('./gray/blackout', cv2.IMREAD_COLOR)

    hsi_control = utils.get_imgs_from_src('./hsi/control', cv2.IMREAD_COLOR)
    hsi_blackout = utils.get_imgs_from_src('./hsi/blackout', cv2.IMREAD_COLOR)

    rgb_control = utils.get_imgs_from_src('./rgb/control', cv2.IMREAD_COLOR)
    rgb_blackout = utils.get_imgs_from_src('./rgb/blackout', cv2.IMREAD_COLOR)

    # Merge the pairs together
    gray_pairs = dict()
    hsi_pairs = dict()
    rgb_pairs = dict()

    gray_hist_stack = utils.create_hstacks([gray_control, gray_blackout], '_control_vs_blackout')
    hsi_hist_stack = utils.create_hstacks([hsi_control, hsi_blackout], '_control_vs_blackout')
    rgb_hist_stack = utils.create_hstacks([rgb_control, rgb_blackout], '_control_vs_blackout')

    # Save the images
    utils.save_imgs_to_src_file('./gray/b_vs_c', gray_hist_stack)
    utils.save_imgs_to_src_file('./hsi/b_vs_c', hsi_hist_stack)
    utils.save_imgs_to_src_file('./rgb/b_vs_c', rgb_hist_stack)




