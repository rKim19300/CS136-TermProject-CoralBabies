# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Hough line detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Hough line detector on these three sets of images

The opposite trend to what I saw with the edge detectors is apparent here. The histogram equalized images preformed poorly, with lines overlapping the voids, while the original image traced the outlines of the void much more accurately. That being said, I am of a conflicting mindset regarding whether these results are worth pursuing. 

On one hand, the lines could be used as contours for a potential flood fill. On the other hand, a lot of the lines seem to be focused on the background, and the trends seem to be pointing towards using the histogram equalized images.