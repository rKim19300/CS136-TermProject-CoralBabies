# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Laplacian edge detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Laplacian edge detector on these three sets of images

As with Canny, applying the Laplacian edge detector on the histogram equalized images yields much more information than the base images.

What's interesting here is that it becomes much easier to judge both the number and the area covered by the coral babies from eye, as compared to the results from the Canny edge detector, as the contrast appears to be much greater.

However, from a computing standpoint, I think that deriving any useful information from these images may be more difficult. Unlike Canny, the voids are polluted with a large amount of errata, to such a degree that we would certainly have to take their impact on area into consideration.

In my opinion, this is is almost certainly due to the additional 3x3 mean blur that Canny underwent. It's pretty clear to me that the next step is to look at how we're going about blurring, such that we start from a consistent base.
