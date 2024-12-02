import cv2
import numpy as np
from src.utils import utils
from cv2 import UMat
import os


MIN_COMPONENT_SIZE = 100

# Its Blue, Green, Red in openCV
WINDOWS_EDIT_BLUE_VAL = np.array([186, 81, 0])


def get_colony_components(colony_map_path: str) -> dict[str, tuple[np.ndarray, dict[np.int64, np.ndarray]]]:
    """
        Uses the marked_colony_maps to get the colonies of each sample as
        connected components

        :colony_map_path: The path to the colony map. We do this since the path is relative to
                          the directory it is called

        :returns: A dictionary with the name of each sample as the key
                  and a tuple containing the map of the pixels, as well as
                  another dictionary that holds <component_label, component_pixel_locations>
    """

    # Load the dataset
    result = dict()
    marked_colony_maps = utils.get_imgs_from_src(colony_map_path, 0)

    # For each colony map, find the connected components
    for name, img in marked_colony_maps.items():
        component_tuple = get_connected_components(img)
        result[name] = component_tuple

    return result


def get_connected_components(img: np.ndarray) -> tuple[np.ndarray, dict[np.int64, np.ndarray]]:
    """
        Gets the connected components of a single image
    """

    # run the connected component algorithm on them
    print('\nGetting the connected components . . . \n')
    num_labels, labels, _, _ = cv2.connectedComponentsWithStats(img, connectivity=8)

    # create a dict of the pixel locations of all the connected components
    print('\nGetting the pixel locations of each component . . . \n')
    components = {}
    for label in range(1, num_labels):  # Skipping label 0 (background)
        component_pixels = np.argwhere(labels == label)
        components[label] = component_pixels

    # Remove the components below a threshold
    print('\nRemoving components below a certain size . . . \n')

    labels_to_remove = []

    for label, pixel_locations in components.items():
        if (len(pixel_locations) < MIN_COMPONENT_SIZE):
            labels_to_remove.append(label) # Remove the label later in the next loop

    # Find the label that contains the black background
    labels_to_remove[labels[0, 0]]
    labels[labels == labels[0, 0]] = 0

    for label in labels_to_remove:
        del components[label]
        labels[labels == label] = 0

    return labels, components


def convert_to_binary(dataset: dict[str, np.ndarray], save_path: str):
    for name, img in dataset.items():
        ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        dataset[name] = binary
    utils.save_imgs_to_src_file(save_path, dataset)


def save_components_for_dataset(dataset: dict[str, np.ndarray], save_path: str):

    for name, img in dataset.items():
        labels, components = get_connected_components(img)
        print(f'{name} has {len(components)} components')

        labeled_img = np.zeros((labels.shape[0], labels.shape[1], 3), dtype=np.uint8)
        colors = np.random.randint(0, 255, size=(len(components), 3), dtype=np.uint8) # generate a random color
        colors[0] = [0, 0, 0]

        # Color each component
        print('\nColoring each component . . .\n')
        for i, label in enumerate(components.keys()):
            labeled_img[labels == label] = colors[i]

        # save the image
        split_name = os.path.splitext(name)
        cv2.imwrite(f'{save_path}/{split_name[0]}_components{split_name[1]}', labeled_img)





if __name__ == '__main__':

    # Convert the dataset to binary (We will mark it in a different tool)
    #dataset = utils.get_imgs_from_src('./canny_colony_map_prepare', 0)
    #convert_to_binary(dataset, './canny_colony_map_prepare')

    # Convert the drawn on samples to binary again
    #dataset_drawnon = utils.get_imgs_from_src('./canny_colony_map_prepare/drawn_on', 0)
    #convert_to_binary(dataset_drawnon, './canny_colony_map_prepare')

    # Generate the colony maps by inverting the images
    #dataset_prepare = utils.get_imgs_from_src('./canny_colony_map_prepare', 0)
    #for name, img in dataset_prepare.items():
    #    dataset_prepare[name] = 255 - img
    #utils.save_imgs_to_src_file('./canny_colony_map', dataset_prepare)

    # Get the connected components of each map, then color and save them
    #canny_colony_map = utils.get_imgs_from_src('./canny_colony_map', 0)

    # Convert the blue values (0, 81, 186) to white and non-blue to black
    """
    marked_colonies = utils.get_imgs_from_src('../../marked_colonies', cv2.IMREAD_COLOR)
    lower_bound = np.clip(WINDOWS_EDIT_BLUE_VAL - 1, 0, 255)
    upper_bound = np.clip(WINDOWS_EDIT_BLUE_VAL + 1, 0, 255)

    for name, img in marked_colonies.items():
        mask = cv2.inRange(img, lower_bound, upper_bound)
        result_img = np.zeros_like(img)
        result_img[mask == 255] = [255, 255, 255]
        marked_colonies[name] = result_img

    # Save the black-white marked colonies
    utils.save_imgs_to_src_file('./marked_colony_map', marked_colonies)
    marked_colonies = utils.get_imgs_from_src('./marked_colony_map', cv2.COLOR_GRAY2BGR)
    convert_to_binary(marked_colonies, './marked_colony_map')
    """

    marked_colonies = utils.get_imgs_from_src('./marked_colony_map', cv2.IMREAD_GRAYSCALE)
    save_components_for_dataset(marked_colonies, './marked_colony_map/components')




