# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from astropy.io import fits
  
def load_fits(file):
  hdulist = fits.open(file)
  data = hdulist[0].data
  length = data.shape
  arr_data = np.array(data)
  ind = np.unravel_index(np.argmax(arr_data),data.shape)
  return ind
  

"""plt.imshow(data, cmap = plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()"""

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 
