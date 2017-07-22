#taking it all in
import psycopg2
def select_all(data):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM ' + data + ';')
  records = cursor.fetchall()
  return records
  
#a proper median
import psycopg2
import numpy as np

def column_stats(table, col):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute("SELECT " +col+ " From " +table+";")
  records = cursor.fetchall()
  arr = np.array(records)
  mean = np.mean(arr[:,0])
  median = np.median(arr[:,0])
 
  return (mean, median)

if __name__ == "__main__":        
  mean, median = column_stats('Star', 't_eff')    
  print (mean, median)
 
 #simple queries in python 1
 # Write your query function here
import numpy as np

def query(file):
  stars = np.loadtxt(file, delimiter=',', usecols=(0,2))
  f_stars = stars[stars[:,1]>1, :] 
  out = np.zeros((1,1))
  
  return f_stars
    



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  
 #simple queries 2
 # Write your query function here
import numpy as np

def query(file):
  stars = np.loadtxt(file, delimiter=',', usecols=(0,2))
  
  f_stars = stars[stars[:,1]>1, :] 
  s_stars = f_stars[np.argsort(f_stars[:, 1]), :] 
  out = np.zeros((1,1))
  
  return s_stars

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  
#simple queries 3
# Write your query function here
import numpy as np
def query(file1, file2):
  stars = np.loadtxt(file1, delimiter=',', usecols=(0,2))
  planets = np.loadtxt(file2, delimiter=',', usecols=(0,5))
  
  f_stars = stars[stars[:,1] > 1, :] 
  s_stars = f_stars[np.argsort(f_stars[:, 1]), :] 
  
  final = np.zeros((1, 1))
  out = np.array([])
  for i in stars:
    for j in planets:
      if (i[0] == j[0]) & (i[1] > 1.0):
        ratio = j[1] / i[1]
        out = np.append(out,ratio)
      outs = np.sort(out)
      outs = outs.reshape(outs.shape[0],1)
  return outs
                 
  
  
""" 
 for i in range(s_stars.shape[0]):
    kepler_id = s_stars[i, 0]
    s_rad = s_stars[i, 1]

    match = planets[np.where(planets[:, 0] == kepler_id), 1].T
    ratio = match/s_rad
    final = np.concatenate((final, ratio))
  
  return final[1:]
"""

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
