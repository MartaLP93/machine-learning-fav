import numpy as np

def maxOfArray(arr):
  return np.max(arr)


listval = np.array([2,4,5,6,7,8])

maxVal = maxOfArray(listval)
print(maxVal)