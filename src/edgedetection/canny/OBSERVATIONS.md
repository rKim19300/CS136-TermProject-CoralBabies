# Initial Observations

## Author(s): Philo Wong, Reece Kim

## Created: 11/29/2024

## Last Edited: 11/30/2024

- Below are observations purely based on visual observations.
- The Canny edge detector was applied on three sets of images: the base images, histogram equalization, and CLAHE, which builds upon histogram equalization
- I will be evaluating the effects of the Canny edge detector on these three sets of images

### Canny process: 

The general trend that I notice is that edge identification is much more sparse when Canny is applied to the base images, as compared to the results obtained from histogram equalized images. This makes sense, as histogram equalization increases the contrast of the images, making edges stand out more.

There are some promising results from Canny edge detection. Although not much can be derived from applying Canny on the base images, it appears that for the histogram equalized images, the "voids" that are produced by Canny edge detection does have a correspondence with the presence of coral babies. 

There are still visible challenges I can see, however. Many of these voids are interconnected, which doesn't aid in counting the number of coral babies, and the edge detector isn't very consistent in fencing off these voids, meaning that area does bleed into the background. Therefore, a simple flood fill of voids greater than a certain threshold would face some complications.

### Inverted Canny: 

- **Reason**: Perhaps inverting the image could make the coral spawn more visible.

![alt text](./he_vs_invhe_vs_labeled/32_T2_6_timepoint0_equalized_compare.JPG)

![alt text](./he_vs_invhe_vs_labeled/32_T2_6_timepoint1_equalized_compare.JPG)

- As can be seen from these two comparisons of a timepoint0 and a timepoint1 image, 
  the inverted he canny image seems to be both darker, and the colonies seem to be less visible, 
  which directly opposes my hypothesis.  

### Inverted Canny (Conclusion)

- We likely can't use the inverted version further, but we may be able to use the non-inverted he-canny 
  samples.  
- If we expand and shrink the HE-canny samples we may be able to clear out some of the noise, then we can 
  find the connected components as the colonies of the image (clearing out connected components that are too small). 
- Prof. Heller's AI algorithm apparently stores the (x, y) coordinates of each colony so
  this gives us an easy we to find the pixel locations of each colony without manually finding the pixel locations 
  ourselves. 
- With this, we would then be able to apply Histogram Equalization on only the colonies.


  


