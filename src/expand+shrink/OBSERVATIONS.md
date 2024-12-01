# Initial Observations
## Author(s): Reece Kim
## Created: 11/30/2024
## Last Editied: 11/30/2024

### Purpose

- To see if expand and shrink will aid in the finding the colonies 
  as connected components

- Order of images:
  1. Original HE_canny
  2. HE_canny with one expansion
  3. HE_canny with e-s-s-e (e = expand, s = shrink)

# Results

![alt text](../edgedetection/canny/hist_equ/32_T2_6_timepoint0_equalized.JPG) 
![alt text](./k3x3_e/32_T2_6_timepoint0_equalized.JPG)
![alt text](./k3x3_e-s-s-e/32_T2_6_timepoint0_equalized.JPG)  

- For the 32 sample at timepoint0, the 3rd image (e-s-s-e), seems to have made the 
  voids between the colonies worse.
- The 2nd image, which only expands it, seems to have done a good job at 
  filling in some of the voids. Compared to the original image

![alt text](../edgedetection/canny/hist_equ/32_T2_6_timepoint1_equalized.JPG) 
![alt text](./k3x3_e/32_T2_6_timepoint1_equalized.JPG)
![alt text](./k3x3_e-s-s-e/32_T2_6_timepoint1_equalized.JPG) 

- Once again 3rd performed poorly, and the 2nd seems to be good a filling in the voids

![alt text](../edgedetection/canny/hist_equ/35_T2_5_timepoint0_equalized.JPG) 
![alt text](./k3x3_e/35_T2_5_timepoint0_equalized.JPG)
![alt text](./k3x3_e-s-s-e/35_T2_5_timepoint0_equalized.JPG) 

- This is the 35 image for timepoint1
- The 2nd image, which is expanded once, seems like it could be filling the voids
  a little bit too much, but it still seems to fill in the voids decently.

### Conclusion

- We can likely use the images that are expanded once
  for the connected components algorithm. 
- We can also likely use a white or black paint too to close or open some of the
  colonies since we are only trying to simulate Prof. Heller's AI algorithm.



