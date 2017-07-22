# Write your import_bss function here.
import numpy as np
def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  ra = 15 * (cat[:,0] + (cat[:,1]/60 + (cat[:,2])/3600))
  dec = np.sign(cat[:,3]) * (np.abs(cat[:,3]) + cat[:,4]/60 + cat[:,5]/3600)
  cats = []
  for c in range(cat.shape[0]):
    cats.append((c+1, ra[c], dec[c])) 
  return cats

#super uses ra in dec degrees 1 , dec in decimal2 , 3: other data
def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  cats = []
  for r in range(len(cat)): #gets rows
    obj = cat[r]
    ra,dec = tuple(obj) #tuple w coordinates
    data = (r+1,ra,dec) #gets what we want
    cats.append(data)
  return cats



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
