import numpy as np
print(np.__version__)

#---------------------------------------------------------------------------------------#
#Python Native Lists vs. Numpy Arrays

myNativeList = [1,2,3]
myNativeList *= 2 #Duplicates Elements
print(myNativeList) #Output: [1,2,3,1,2,3]

numpyArray = np.array([1,2,3,4])
numpyArray *= 2 #Multiplies each element by 2
print(numpyArray) #Output: [2,4,6,8]
print(type(numpyArray)) #Class: numpy.ndarray: an N-Dimensional Array

#To get a similar output like native lists with numpy arrays, we use np.tiles()
numpyArray = np.array([1,2,3,4])
repeatedArray = np.tile(numpyArray, 2) #np.tile(target array, number of times to be duplicated)
print(repeatedArray)#Output: [1 2 3 4 1 2 3 4]


#------------------------------------------------------------------------------------------#
#Numpy Multidimensional Arrays
