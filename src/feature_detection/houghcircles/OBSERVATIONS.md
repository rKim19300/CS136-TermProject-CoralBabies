# Initial Observations

## Author(s): Philo Wong

## Created: 11/29/2024

## Last Edited: 11/29/2024

- Below are observations purely based on visual observations.
- The Hough circle detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Hough circle detector on these three sets of images

The Hough circle transform appears to perform very poorly on the dataset, which is disappointing, as I considered it to be one of the more promising algorithms that we might be able to apply. This was perhaps best demonstrated when the transform was applied to the satellite image of Lake Tahoe. There, the algorithm was able to quite consistently identify the diamond overlay generated by Google Earth, but when applied to our coral dataset, very few of the corals could be meaningfully classified. What I can draw from this is that although the Hough transform works very well for regular shapes, such as perfect or nearly perfect circles, it really struggles when handling irregular shapes.