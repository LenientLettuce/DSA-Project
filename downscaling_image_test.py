import random as rand
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math as math
# from image_import import read

def def_mat(n):
    output = np.random.randint(100, size=(n, n))
    return output

def quad_tree(matrix, n, rows, columns): 
    allsame = True
    for i in range(n): 
        if allsame == True:
            for j in range(n):
                if np.all(matrix[rows][columns] != matrix[rows + i][columns + j]):
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
    
    # print((topleft + topright + bottomleft + bottomright) // 4)
    return ((topleft + topright + bottomleft + bottomright) // 4)  # returning average if all not same

img = mpimg.imread(r"dsa_proj\dsatest.jpg")
matrix = img
mat_size = 1024

# original image visualization
plt.imshow(matrix, cmap="gray") 
plt.colorbar()
plt.title("Original Matrix Visualization")
plt.show()


scale_factor = 4

scaled_matrix = np.zeros((mat_size//scale_factor, mat_size//scale_factor))  # new matrix initialization
for i in range(0, mat_size, scale_factor):  # iterating over original matrix
    for j in range(0, mat_size, scale_factor):
        result = quad_tree(matrix, 4, i, j)
        scaled_matrix[i//4][j//4] = result[2]



# scaled image visualization
plt.imshow(scaled_matrix, cmap="gray") 
plt.colorbar()
plt.title("Scaled Matrix Visualization")
plt.show()


