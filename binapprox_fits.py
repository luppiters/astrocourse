# Import the running_stats function
from helper import running_stats
import numpy as np
from astropy.io import fits

# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(filenames, B): #helpful Q in forum: http://bit.ly/2sPGlVR
  #define all variables
  mean, std = running_stats(filenames)
  dim = mean.shape #n_row, n_col
  minarr = mean - std
  maxarr = mean + std
  #count the values < min_value = min_array[i,j]:
  left = np.zeros(dim)
  hist = np.zeros((dim[0], dim[1], B))
  width = (2*std)/B
  #loop over files
  for file in filenames:
    hdulist = fits.open(file) 
    data = hdulist[0].data
    left[data < minarr] += 1
    ind = np.logical_and(data >= minarr, data < maxarr)
    bin_arr = ((data[ind]- minarr[ind])/width[ind]).astype(int)
    hist[ind, bin_arr] += 1 
  return mean, std, left, hist


def median_approx_fits(filenames, B):
  mean, std, left, hist_arr = median_bins_fits(filenames, B)
  N = len(filenames)
  mid = (N + 1)/2
  width = 2 * std / B
  count = left
  dim = mean.shape
  b = np.zeros_like(mean)
  median = np.empty(dim)
  
  for i in range(dim[0]):
    for j in range(dim[1]):
      for k, bincount in enumerate(hist_arr[i,j,:]):
        count[i,j]+= bincount
        if count[i,j] >= mid:
          median[i, j] = mean[i, j] - std[i, j] + width[i, j]*(k + 0.5)
          hist_arr[i, j] = k
          break
  return median


""" quicker alternative:
for b in range(B):   
    count += hist_arr[:,:,b]
    g_ind = (count >= mid)
    median[g_ind] = mean[g_ind] - std[g_ind] + (width[g_ind]*(b + 0.5))
    count[g_ind] = -1E8
  """

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
