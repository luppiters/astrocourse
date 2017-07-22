# Write your find_closest function here
import numpy as np
def angular_dist(r1_r, d1_r, r2_r, d2_r):
  r1 = np.radians(r1_r)
  d1 = np.radians(d1_r)
  r2 = np.radians(r2_r)
  d2 = np.radians(d2_r)
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  d_deg = np.degrees(d)
  return d_deg

def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  ra = 15 * (cat[:,0] + (cat[:,1]/60 + (cat[:,2])/3600))
  dec = np.sign(cat[:,3]) * (np.abs(cat[:,3]) + cat[:,4]/60 + cat[:,5]/3600)
  cats = []
  for c in range(cat.shape[0]):
    cats.append((c+1, ra[c], dec[c])) 
  return cats

def find_closest(cat, ra_s, dec_s):
  ra = [x[1] for x in cat] #from our catalogues
  dec = [x[2] for x in cat]
  adis = angular_dist(ra_s, dec_s, ra, dec) #ang dist btwn cat and source
  dist = np.amin(adis[:])
  ind = np.argmin(adis[:]) + 1
  return ind, dist
  
  



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
