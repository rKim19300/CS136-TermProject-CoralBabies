# Initial Observations

## Author(s): Philo Wong

## Created: 12/1/2024

## Last Edited: 12/1/2024

- Below are observations purely based on visual observations.
- The Mean smoothing filter was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Mean smoothing filter set to a 3x3 frame on these three sets of images

The Mean smoothing filter does visibly smooth the image. However, its effect is sort of counteractive to what our previous histogram equalization aimed to accomplish. In particular, due to edges and voids often coexisting next to each other, the result is that the overall contrast decreases.