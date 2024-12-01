# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Gaussian smoothing filter was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Gaussian smoothing filter set to a 3x3 frame on these three sets of images

I will be mainly focused on how well the Gaussian smoothing filter performs in eliminating noise from within the coral babies. The contrast is much greater and more readable when applied to the histogram equalized images, but that is to be expected.

The effect of the Gaussian filter appears to be to concentrate the errata, which perhaps explains the random noise that the Laplacian edge detector experienced? I'm not sure this is the right way forward.
