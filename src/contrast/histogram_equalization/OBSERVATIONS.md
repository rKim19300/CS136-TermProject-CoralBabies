# Initial Observations
## Author(s): Reece Kim
## Created: 11/19/2024
## Last Editied: 11/19/2024

- Below are observations purely based on visual observations.
- The images from left to right are
  - The original sample
  - The original sample in gray scale
  - The sample after histogram equalization that has been marked
  - The original sample manually marked.

### 32_T2_6_timepoint0_equalized.JPG

![alt text](./hstack/32_T2_6_timepoint0_equalized_compare.JPG)

- The histogram equalization (HE) did seem to make the coral spawn 
  more visible with a few caveats.
- The coral spawn in the first circle, which was not caught in the manual labeling,
  compared to both the original and grayscale seems to be more visible.
- In the 2nd circle, a coral spawn whose background was the dark black 
  background is not visible in the image in which HE was applied.
- In the 3rd circle, It seems like the coral spawn could possibly blend in 
  with the background and perhaps confuse an algorithm, but further testing has 
  to be done.
- In the 4th circle, a segmentation algorithm could possibly confuse the noise
  with a coral spawn if it is only accounting for intensity.

### 32_T2_6_timepoint1_equalized.JPG

![alt text](./hstack/32_T2_6_timepoint1_equalized_compare.JPG)

- In circle 1, we can see that the spawn have distinguishable texture at 
  timepoint1, in which there are little white dots that circle around the spawn.
- In circle 2, there is a cluster of spawn that is meshed together, but the white
  dot can still be used to distinguish them, so an algorithm that is perhaps able to 
  detect this texture would be good.  
- Perhaps this is a special case, or my observation is wrong, but there seems to be 
  less noise that could be mistaken for the spawn than at timepoint0.

### 33.5_T1_4_timepoint0_equalized.JPG

![alt text](./hstack/33.5_T1_4_timepoint0_equalized_compare.JPG)

- My observations are similar to the image at the last at timepoint0.

### 33.5_T1_4_timepoint1_equalized.JPG

![alt text](./hstack/33.5_T1_4_timepoint1_equalized_compare.JPG)

- The 1st circle show that I may have circled a dead spawn in my manual
  labeling, this one seems to be much lighter unlike the other spawn at timepoint1.
- The 2nd circle shows a small spawn in a cluster that does not have the 
   white marks and might be missed if we only look for the white marks.

### 35_T2_5_timepoint0_equalized.JPG

![alt text](./hstack/35_T2_5_timepoint0_equalized_compare.JPG)

- In the 1st circle, the spawn are more visible, but then don't seem 
  very distinct, so they might be hard for an algorithm to count. 
- In the 2nd circle, the spawn seem to be more visible, but is also very faded.

### 35_T2_5_timepoint1_equalized.JPG

![alt text](./hstack/35_T2_5_timepoint1_equalized_compare.JPG)

- Circle 1 and 2 show spawn that don't have the white dots in 
  them, meaning we can't rely solely on those dots.
- Circle 3 is a piece a circular noise that could easily be mistaken for a spawn.
  My earlier observation about the noise is likely not fully true.
- Circle 4 seems to be a coral spawn that could easily be mistaken for
  noise. 