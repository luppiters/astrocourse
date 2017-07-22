# Write your crossmatch function here.
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

def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  cats = []
  for r in range(len(cat)): 
    obj = cat[r]
    ra,dec = tuple(obj) 
    data = (r+1,ra,dec) 
    cats.append(data)
  return cats

def find_closest(cat, ra_s, dec_s):
  ra = [x[1] for x in cat] 
  dec = [x[2] for x in cat]
  adis = angular_dist(ra_s, dec_s, ra, dec)
  dist = np.amin(adis[:])
  ind = np.argmin(adis[:]) + 1
  return ind, dist

def crossmatch(cat1, cat2, max_dist):
  no = []
  yes = []
  for id1, ra1, dec1 in cat1: #first catalogue
    cldist = np.inf
    cl_id2 = None
    for id2, ra2, dec2 in cat2: #crossmatching with second
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < cldist:
        cl_id2 = id2
        cldist = dist
    if cldist > max_dist:
      no.append(id1)
    else:
      yes.append((id1, cl_id2, cldist))
        
  return yes, no

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
