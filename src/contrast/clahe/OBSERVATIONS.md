# Initial Observations
## Author(s): Reece Kim
## Created: 11/27/2024
## Last Edit: 11/27/2024

### Reason for choosing CLAHE

- CLAHE breaks the images up into tiles and then
  attempts performs local he on each tile.
- CLAHE also attempts to reduce noise by, if one 
  bin goes over the clip limit, spreading the excess into other bins
- The above might reduce the amplification of the noise
  and do a better job at amplifying the coral spawn

## Visual Observations

- Below are observations purely based on visual observations.
- The images from left to right are
  - The original sample
  - The original sample in gray scale
  - The sample after histogram equalization
  - The sample after clahe is applied with
  - The original sample manually marked.

### 32_T2_6_timepoint0_clahe_cl40_tgs8x8.JPG

![alt text](./hstacks/32_T2_6_timepoint0_clahe_cl40_tgs8x8_compare.JPG)

- Blue: If you look closely, the spawn whose on the black background
        instead of the nail is slightly darker in the clahe photo, suggesting
        that clahe could perform worse with images that have many spawn with a
        similar background.
- Green: Although CLAHE seems to make the spawn darker compared to its background
         than regular HE, it also could make it harder to distinguish how many 
         individuals are in a colony or if the black blob is just noise.
- Orange: CLAHE seems to also amplify some noise when in gray scale. Though notice
          how the noise is a different color than the colonies. Perhaps
          **in the future** we could try to only amplify a certain hue range.
- Red: CLAHE seems to become more dull around the edges since the black background is
       likely making it go past the clip limit. If we decide to tune the parameters of CLAHE,
       then we should likely choose a smaller tileGridSize.

### 32_T2_6_timepoint1_clahe_cl40_tgs8x8.JPG

![alt text](./hstacks/32_T2_6_timepoint1_clahe_cl40_tgs8x8_compare.JPG)

- Red: Once again, CLAHE seems to perform worse than HE around the edges of the sample, 
       suggesting we would have to reduce the tileGridSize in the future.
- Blue: Overall, it seems that CLAHE might generally work better than HE for timepoint1.
        This is because the spawn have characteristic dot within them that make the distinguishable
        from each other at timepoint1. 

### 33.5_T1_4_timepoint0_clahe_cl40_tgs8x8

![alt text](./hstacks/33.5_T1_4_timepoint0_clahe_cl40_tgs8x8_compare.JPG)

- Blue: The intensity change in CLAHE seems to be less consistent for this colony
        compared to HE.  This could confuse some segmentation and feature detection algorithms.

### 33.5_T1_4_timepoint1_clahe_cl40_tgs8x8

![alt text](./hstacks/33.5_T1_4_timepoint1_clahe_cl40_tgs8x8_compare.JPG)

- Blue: The noise seems to be of a more similar intensity of the coral spawn in CLAHE
  than in HE.
  - Could a bigger window + bigger cliplimit perform better?

### 35_T2_5_timepoint0_clahe_cl40_tgs8x8

![alt text](./hstacks/35_T2_5_timepoint0_clahe_cl40_tgs8x8_compare.JPG)

- Blue: The spawn here see to blend less with their background than it does for 
        HE, which could be good for certain segmentation of feature detection 
        algorithms that rely on intensity thresholding. 

### 35_T2_5_timepoint1_clahe_cl40_tgs8x8

![alt text](./hstacks/35_T2_5_timepoint1_clahe_cl40_tgs8x8_compare.JPG)

- Blue: The dots within this spawn seem to be less visible in CLAHE than it is in HE.
- Red:  This noise seems to be more amplified in CLAHE than in the HE sample.

### Overall

- CLAHE seems like it could be doing a good job in terms of amplifying the spawn more than
  HE, but it also seems like it might end up creating more false positives. 

- We might want to start looking into less naive way of increasing the contrast. 

- Ideas:
    - Seeing if the spawn of a certain Hue (in HSI) and increasing that specific hue. 
    - Applying HE or CLAHE to the samples in color, but perhaps only select one or two of the rgb channels
