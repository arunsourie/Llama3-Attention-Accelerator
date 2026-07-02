
#Task -1
#Dot Product

import numpy as np

Q = np.array([1, 2, 3])
K = np.array([4, 5, 6])

dot_product = np.dot(Q, K)

print("Dot Product:", dot_product)
#OUTPUT:- 32




#Task-2
#perform Q × Kᵀ

import numpy as np

Q = np.array([[1, 2]])
K = np.array([[2, 3]])

scores = Q @ K.T

print(scores)

#OUTPUT:- [[8]]

