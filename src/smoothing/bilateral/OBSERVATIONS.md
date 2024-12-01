# Initial Observations

## Author(s): Philo Wong

## Created: 11/30/2024

## Last Edited: 11/30/2024

- Below are observations purely based on visual observations.
- The Bilateral smoothing filter was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Bilateral smoothing filter with a sigma set to 2 on these three sets of images

Our images, especially the ones which have been preprocessed with histogram equalization, are completely cluttered with edges, which Bilateral smoothing attempts to spare. The result is that very little smoothing occurs at all.
