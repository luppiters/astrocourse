# Write your crossmatch function here.
import numpy as np
import time
def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  d_deg = np.degrees(d)
  return d_deg

def crossmatch(cat1, cat2, max_rad):
  start = time.perf_counter()
  new = []
  fin = []
  no_match = []
  
  for i, x in enumerate(cat1):
    new_matches = []
    min_dist = np.inf
    ra1 = np.radians(x[0])
    d1 = np.radians(x[1])
    for j, y in enumerate(cat2):
      ra2 = np.radians(y[0])
      d2 = np.radians(y[1])
      dist = angular_dist(ra1, d1, ra2, d2)
      if dist < min_dist:
        min_id2 = j
        min_dist = dist
    if min_dist <= max_rad:
      new.append(i)
      fin.append((i, min_id2,min_dist))
    else:
      no_match.append(i)
      
  taken = time.perf_counter() - start 
  return fin, no_match, taken

""""
  new1 = []
  new2 = [] 
  final = []
  no_match = []
  for i, x in enumerate(cat1):
    min_dist = np.inf
    new_RA = np.radians(x[0])
    new_Dec = np.radians(x[1])
    new_cat1.append((i, new_RA, new_Dec))
    for j, y in enumerate(cat2):
      new_RA_cat2 = np.radians(y[0])
      new_Dec_cat2 = np.radians(y[1])
      new_cat2.append((j, new_RA_cat2, new_Dec_cat2))
    for x in new_cat1:
        doot = len(final_cat)
    for y in new_cat2: 
          distance = angular_dist(y[1], y[2], x[1], x[2]) 
    if distance <= max_rad and distance < min_distance:   
      min_distance = distance       
      final_cat.append((x[0], y[0], distance))
    elif len(final_cat) == doot:  
      unmatched.append(x[0])   
  
  timeTaken = time.perf_counter() - start  
              
  return final_cat, unmatched, timeTaken
        """
 

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
