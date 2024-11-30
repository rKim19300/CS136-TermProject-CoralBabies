# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Canny edge detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Canny edge detector on these three sets of images

Canny process: 

The general trend that I notice is that edge identification is much more sparse when Canny is applied to the base images, as compared to the results obtained from histogram equalized images. This makes sense, as histogram equalization increases the contrast of the images, making edges stand out more.

There are some promising results from Canny edge detection. Although not much can be derived from applying Canny on the base images, it appears that for the histogram equalized images, the "voids" that are produced by Canny edge detection does have a correspondence with the presence of coral babies. 

There are still visible challenges I can see, however. Many of these voids are interconnected, which doesn't aid in counting the number of coral babies, and the edge detector isn't very consistent in fencing off these voids, meaning that area does bleed into the background. Therefore, a simple flood fill of voids greater than a certain threshold would face some complications.
