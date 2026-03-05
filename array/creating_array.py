import numpy as np

arr = np.array([], dtype = int) #declaring an array 
arr = np.append(arr, [1,2,3,4])
print(arr)


import array

arr2 = array.array("i",[1,2,3,4])   #declaring and initializing an array

print(arr2)


arr2.insert(4,5) # array insertion

print(arr2)