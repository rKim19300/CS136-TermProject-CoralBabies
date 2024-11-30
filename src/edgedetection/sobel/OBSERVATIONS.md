# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Sobel edge detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Sobel edge detector on these three sets of images

Much the same as Laplacian. The voids are distinct, but there is errata cluttering the voids. More smoothing is required.

What I will note is that the errata in the void appears to be more connected, forming a set of contours. This is very much preferable to the random white noise which Laplacian was spitting out, as you're filtering out units rather than individual pixels.
