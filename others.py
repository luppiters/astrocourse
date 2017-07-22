#TIME IT!
import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array should not be included
  data = np.random.rand(size)
  # modify this function to time func with ntrials times using a new random array each time
  start = time.perf_counter()
  for i in range(ntrials):
    res = func(data)
  # return the average run time
  avgrt = (time.perf_counter() - start)/ntrials
  return avgrt

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))


#comparison mean and median
# Write your list_stats function here.
import numpy as np
def list_stats(n):
  mean = np.mean(n).round(3)
  median = np.median(n)
  return (median, mean)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
  
#mean 1d array
import numpy as np
# Write your calc_stats function here.
def calc_stats(filename):
  data = np.loadtxt(filename, delimiter=',')
  mean = np.round(np.mean(data), 1)
  median = np.round(np.median(data), 1)
  return (mean, median)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  print(mean)
  
#mean list
# Write your calculate_mean function here.
def calculate_mean(f):
  return sum(f) / len(f)
  
  
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  
 
