import numpy as np
print(np.__version__)

#---------------------------------------------------------------------------------------#
#Python Native Lists vs. Numpy Arrays
#NOTE: numpy arrays require a consistent number of elements within each of their subset lists
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

#Zero Dimension Arrays
Zeroarray = np.array("A") #0 Dimension array
print(Zeroarray.ndim) #ndim attribute returns the dimension of numpy arrays

#One Dimension Array
OneArray = np.array(["A", "B", "C"]) #1 Dimension array
print(OneArray.ndim)

#Two Dimension Array
TwoArray = np.array([["A", "B", "C"],
                     ["D", "E", "F"],
                     ["G", "H", "I"]]) #2 Dimension array
print(TwoArray.ndim)

#And similarly more can be defined