# Write your function median_FITS here:
import sys
import numpy as np
import time
from astropy.io import fits

def median_fits(filenames):
  start = time.perf_counter()
  fitslist = []
  for filename in filenames:
    hdulist = fits.open(filename)    
    data = hdulist[0].data    
    fitslist.append(data)
    hdulist.close()
  stack = np.dstack(fitslist)
  median = np.median(fitslist, axis=0)
  memory = (stack.nbytes) / 1024
  seconds = time.perf_counter() - start  
  
  return median, seconds, memory


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
