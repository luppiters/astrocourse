# Write your hms2dec and dms2dec functions here
def hms2dec (h, m, s):
  conv = 15 * (h + m/60 + s/3600)
  return conv
def dms2dec (d, m, s):
  if d < 0:
    conv = -1* (-d + (m/60 + s/3600))
  else:
    conv = d + (m/60 + s/3600)
  return conv

#1 min in hms = 15' in dms, 1 sec = 15''

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))
