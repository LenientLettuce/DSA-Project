import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from helper import *

def quad_tree(matrix, n, rows, columns): 
    allsame = True
    for i in range(n): 
        if allsame == True:
            for j in range(n):
                if abs(matrix[rows][columns] != matrix[rows + i][columns + j]):
                    allsame = False
                    break
        else:
            break

    if allsame: 
        return matrix[rows][columns]  # returning original value if allsame

    n = n//2 
    topleft = quad_tree(matrix, n, rows, columns)
    topright = quad_tree(matrix, n, rows, columns+n)
    bottomleft = quad_tree(matrix, n, rows+n, columns)
    bottomright = quad_tree(matrix, n, rows+n, columns+n)
    
    return (topleft + topright + bottomleft + bottomright) // 4  # returning average if all not same

mat_size = 512 # also try 256, creates more varied result
               # higher values have issue of diluting into pink, but zooming in reveals that detail is still there
matrix = def_mat(mat_size,mat_size)

# original image visualization
plt.imshow(matrix, cmap="plasma") 
plt.colorbar()
plt.title("Original Matrix Visualization")
plt.show()


scale_factor = 4

scaled_matrix = np.zeros((mat_size//scale_factor, mat_size//scale_factor))  # new matrix initialization
for i in range(0, mat_size, scale_factor):  # iterating over original matrix
    for j in range(0, mat_size, scale_factor):
        scaled_matrix[i//4][j//4] = quad_tree(matrix, 4, i, j) 

# scaled image visualization
plt.imshow(scaled_matrix, cmap="plasma") 
plt.colorbar()
plt.title("Scaled Matrix Visualization")
plt.show()
