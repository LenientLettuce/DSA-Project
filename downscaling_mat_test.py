import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from helper import *

def quad_tree(matrix,r,c,rows,columns,threshold,scaled_mat,scale_factor): #Basic QuadTree Function
    if r <= 1 and c <= 1: #Means image is a single pixel
        return
    if r <= 1: #Ensures recursion doesn't stop until both rows and columns are compressed
        r = 2
    if c <= 1:
        c = 2
    allsame = True
    total = 0
    for i in range(r): #Loop checks whether each element within the quad tree is same or not
        if allsame == True:
            for j in range(c):
                if (rows + i) < matrix.shape[0] and (columns + i) < matrix.shape[1]:
                    total += matrix[rows + i][columns + j]
                    if abs(matrix[rows][columns] - matrix[rows + i][columns + j]) > threshold:
                        allsame = False
                        break
        else:
            break

    if allsame: #if each element is same, then the section is kept as is
        avg = (total)//(r*c)
        for i in range(r):
            for j in range(c):
                if (rows//scale_factor) < scaled_matrix.shape[0] and (columns//scale_factor) < scaled_matrix.shape[1]:
                    scaled_matrix[rows//scale_factor][columns//scale_factor] = avg
        return

    r = r//2
    c = c//2 
    #if each element is not the same, then the section is divided into 4
    topleft = quad_tree(matrix,r,c,rows,columns,threshold,scaled_mat,scale_factor)
    topright = quad_tree(matrix,r,c,rows,columns+c,threshold,scaled_mat,scale_factor)
    bottomleft = quad_tree(matrix,r,c,rows+r,columns,threshold,scaled_mat,scale_factor)
    bottomright = quad_tree(matrix,r,c,rows+r,columns+c,threshold,scaled_mat,scale_factor)

mat_size = 32  # works with any multiple of 4

matrix = def_mat(mat_size,mat_size)

# original image visualization
show(matrix, "Original")

# scaled matrix initialization
scale_factor = 4
scaled_matrix = np.zeros((mat_size//scale_factor, mat_size//scale_factor))

# scaled matrix visualization
quad_tree(matrix, 512, 512, 0, 0, 40, scaled_matrix, scale_factor)
show(scaled_matrix, "Downscaled Matrix")


