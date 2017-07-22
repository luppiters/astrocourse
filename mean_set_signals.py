import numpy as np
# Write your mean_datasets function here
def mean_datasets(filelist):
  files = np.loadtxt(filelist[0],delimiter = ',')
  files = files - files
  for i in filelist: 
    files = files + (np.loadtxt(i,delimiter = ','))
  mean = (files/len(filelist)).round(1)
  return mean
"""
def mean_datasets(filenames):
  data = []
  for i in filenames:
    data += data[i]
    mean = (i/len(filenames)).round(1)
  
  # Step 1 - loop through each filename in the list of filenames
  # Step 2 - load the data from each file into an array (append to an n-dimensional numpy array)
  # Step 3 - calculate the mean of the values in the n-dimensional array
  # Step 4 - round to 1 dp
  return mean"""

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
