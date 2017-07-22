# Write your median_bins and median_approx functions here.
import numpy as np
def median_bins(values, B): #steps 1-6
  values = np.array(values)
  mean = np.mean(values)
  std = np.std(values)
  minval = mean - std
  maxval = mean + std
  witdh = (2*std)/B
  ignored = int(((values < minval) & (values <=maxval)).sum())
  left = int((values < minval).sum())
  new = values[( (minval<=values) & (values < maxval))]
  histo = np.histogram(new, B, range = (minval, maxval))
  bins = histo[0].astype(float)
  return mean, std, left, bins

def median_approx(values, B): #steps 7-8
  mean, std, left, bins = median_bins(values, B)
  minval = mean - std
  maxval = mean + std
  N = len(values)
  mid = (N+1)/2
  count = left
  for b, bincount in enumerate(bins):
    count += bincount
    if count >= mid:
      break

  width = 2*std/B
  median = mean - std + width*(b + 0.5)
  return median
 



# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_bins([0, 1], 5))
  print(median_approx([0,1],5))
