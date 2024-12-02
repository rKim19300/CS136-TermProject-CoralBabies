from src.utils import utils
from collections import OrderedDict
import numpy as np
import os
import cv2


def apply_blob(imgs: dict[str, np.ndarray], name_append: str, params: cv2.SimpleBlobDetector.Params) -> dict[str, np.ndarray]:
    detector = cv2.SimpleBlobDetector_create(params)

    result = dict()
    for name, img in imgs.items():

        keypoints = detector.detect(img) # Detect keypoints in the img
        print(f"Detected {len(keypoints)} keypoints in {name}")

        # Apply blob detection
        img_with_keypoints = cv2.drawKeypoints(img,
                                               keypoints,
                                               np.array([]),
                                               (0, 0, 255),
                                               cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Add to result dict
        name_split = os.path.splitext(name)
        result[f"{name_split[0]}_blob_detect{name_append}{name_split[1]}"] = img_with_keypoints

    return result

def apply_blob_to_data(dataset_path: str, sample_folder: str, hstack_folder:str):
    """
        Apply blob detected to the histogram equalized images. Save the images to their
        respective folder.
    """

    # Load the equalized images
    dataset = utils.get_imgs_from_src(dataset_path, cv2.IMREAD_COLOR)

    # Separate them into separate timepoints
    samples_t0 = dict()
    samples_t1 = dict()
    for name, img in dataset.items():
        if 'timepoint0' in name:
            samples_t0[name] = img
        elif 'timepoint1' in name:
            samples_t1[name] = img

    # Set up the params
    params_t0 = cv2.SimpleBlobDetector_Params()
    params_t0.filterByArea = True
    params_t0.minArea = utils.MIN_AREA_TIMEPOINT0
    params_t0.maxArea = utils.MAX_AREA_TIMEPOINT0
    params_t0.filterByCircularity = True
    params_t0.minCircularity = 0.2
    params_t0.filterByInertia = True # Filter based on distribution of mass around centroid
    params_t0.minInertiaRatio = 0.2  # Closer to 1 means more of a perfect circle

    params_t1 = cv2.SimpleBlobDetector_Params()
    params_t1.filterByArea = True
    params_t1.minArea = utils.MIN_AREA_TIMEPOINT1
    params_t1.maxArea = utils.MAX_AREA_TIMEPOINT1
    params_t1.filterByCircularity = True
    params_t1.minCircularity = 0.2
    params_t1.filterByInertia = True  # Filter based on distribution of mass around centroid
    params_t1.minInertiaRatio = 0.2   # Closer to 1 means more of a perfect circle

    # Apply to timepoint0
    print("applying blob detection to timepoint0 . . . ")
    samples_t0 = apply_blob(samples_t0, f'_A_C{params_t0.minCircularity}_I{params_t0.minInertiaRatio}', params_t0)

    # Apply to timepoint1
    print("applying blob detection to timepoint1 . . . ")
    samples_t1 = apply_blob(samples_t1, f'_A_C{params_t1.minCircularity}_I{params_t1.minInertiaRatio}', params_t1)

    # Create hstacks of the images
    labeled = utils.get_imgs_from_src('../../../labeled_data', cv2.IMREAD_COLOR)
    labeled = OrderedDict(sorted(labeled.items()))
    blob_imgs = OrderedDict(sorted((samples_t0 | samples_t1).items()))

    # Create the hstacks and then save them
    hstacks = utils.create_hstacks([labeled, blob_imgs], '_compare')

    # Save the images
    #utils.save_imgs_to_src_file(hstack_folder, hstacks)
    utils.save_imgs_to_src_file(sample_folder, samples_t0)
    utils.save_imgs_to_src_file(sample_folder, samples_t1)


if __name__ == '__main__':

    # Apply to the base dataset
    #apply_blob_to_data('../../../dataset', './control', './control/hstacks')

    # Apply to the histogram_equalized dataset
    #apply_blob_to_data('../../contrast/histogram_equalization', './hist_eq', './hist_eq/hstacks')

    # Apply to the clahe dataset
    #apply_blob_to_data('../../contrast/clahe', './clahe', './clahe/hstacks')

    #apply_blob_to_data('../../contrast/tahe/nonoise', './tahe', './tahe/hstack')

    #apply_blob_to_data('../../smoothing/median/clahe', './median+blob_clahe', './clahe/hstacks')
    #apply_blob_to_data('../../smoothing/median/equalized', './median+blob_he', './clahe/hstacks')
    apply_blob_to_data('../../segmentation/Mean_Shift/binary_tahe', './binary_ms_tahe', './clahe/hstacks')


