#Marshal Will
#Program will demonstrate munipulation of matrixes

import numpy as np

#transposes matrix
def transposeMatrix(m):
    return np.transpose(m)

#method gets determinant
def getMatrixDeternminant(m):
    return np.linalg.det(m)

#method will call other methods to get inverse of matrix
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

#method returns the minor values of each matrix
def getMatrixMinor(arr,i,j):
    # returns matrix minor for each iteration
    return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
               np.array(list(range(j))+list(range(j+1,arr.shape[1])))]

#method gets determinant values of each matrix
def getMatrixMinorDeterminants(m):
    for r in range(len(m)):
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            return minor


myMatrix = np.array([[7,2,1],[0,3,-1],[-3,4,-2]])
print("Normal Matrix")
print(myMatrix)

print("Inverse of Matrix using a Method and not using Numpy")
print(getMatrixInverse(myMatrix))

InvMyMatrix = np.linalg.inv(myMatrix)
print("Inverse of Matrix using numpy")
print(InvMyMatrix)
