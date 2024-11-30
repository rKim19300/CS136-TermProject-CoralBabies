# Observations
## Author(s): Reece Kim
## Created: 11/29/2024
## Last Editied: 11/29/2024

### Explanation and reason for choice

- There are three kinds of blob detection. 
  - Laplacian of Gaussian 
  - Difference of Gaussian
  - Determinant of Gaussian

- OpenCV's uses a more simplified version of
  blob detection that does not use any of the
  three and instead detects simple shapes.

- **Reason for choice**: 
    - Many of the individuals in the samples aren't
      perfect circles and instead malformed, perhaps
      this algorithm will be able to detect the semi-circle
      objects such of our coral spawn well

- **Parameters Chosen**
    - The parameters chosen filter the samples by 
      minimum inertia ratio a minimum circularity
    - **Minimum Inertia ratio**: The lower the number (between 0 to 1) the more elliptical the
      detected blobs are allowed to be, we have 0.2 so they are allowed to be very elliptical.
      - Equation: ((4 * pi) * Area) / Perimeter
    - **Minimum Circularity**: The lower the circularity (values between 0 to 1) the more malformed the circles are allowed to be.
      Since we chose 0.2, they yare allowed to be very malformed.
      - Equation: (Length of Minor Axis) / (Length of Major Axis)

### Results

- For the base samples, histogram equalized, and clahe datasets, the blob
  detector found nothing. Since the min circularity and inertia ratio was low