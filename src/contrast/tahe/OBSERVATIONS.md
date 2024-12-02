# Initial Observations
## Author(s): Reece Kim
## Created: 12/1/2024
## Last Edit: 12/1/2024

### Explanation

- Targeted Adaptive Histogram Equalization (TAHE) applies histogram equalization to only
  the coral colonies based on a component map.
- It works under the assumption that Prof. Heller's AI algorithm will
  map the colonies a similar way that we did
- The supposed benefits of TAHE are:
  - **Noise reduction**: The noise around the colonies don't get intensified, 
    likely reducing noise. Furthermore, the noise doesn't get added to the equalized 
    histograms of the colonies.

![alt text](../../connected_components/marked_colony_map/components/32_T2_6_timepoint0_components.JPG) 

- We used the colony maps from the connected_components folder to find the colonies as connected components

### Results

![alt text](./compare/32_T2_6_timepoint0_tahe_compare.JPG) 

![alt text](./compare/32_T2_6_timepoint1_tahe_compare.JPG) 

- Although the noise around the coral spawn is less intense, 
  at both timepoints 0 and 1, the spawn themselves are less solid 
  and are more blended in with their backgrounds.
- Though the difference in intensities between the spawn and the non-HEed 
  background might be just enough for an edge detector to separate the spawn well
  and perhaps have canny circles applied to them. 