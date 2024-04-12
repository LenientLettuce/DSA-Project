import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from helper import *

def quad_tree(matrix,r,c,rows,columns,threshold,scaled_mat,scale_factor): #Basic QuadTree Function
    if r <= 1 or c <= 1: #Means one or more dimension/s of image is only single hence image cannot be divided into 4
        if r <= 1 and c <= 1: #means both dimensions are only single pixels
            pass
        elif r <= 1: #means rows are single pixel
            pass    
        elif c <= 1: #means columns are single pixel
            pass
        return
    allsame = True
    total_r = total_g = total_b = 0
    for i in range(r): #Loop checks whether each element within the quad tree is same or not
        if allsame == True:
            for j in range(c):
                if (rows + i) < matrix.shape[0] and (columns + i) < matrix.shape[1]:
                    total_r += matrix[rows + i][columns + j][0]
                    total_g += matrix[rows + i][columns + j][1]
                    total_b += matrix[rows + i][columns + j][2]
                    if len(matrix[rows][columns]) == 1:
                        if abs(matrix[rows][columns] - matrix[rows + i][columns + j]) > threshold:
                            allsame = False
                            break
                    else:
                        total_diff = 0
                        for k in range(2):
                            total_diff += abs(float(matrix[rows][columns][k]) - float(matrix[rows + i][columns + j][k]))
                        if total_diff//3 > threshold:
                            allsame = False
                            break
        else:
            break

    if allsame: #if each element is same, then the section is kept as is
        avg_r = (total_r)//(r*c)
        avg_g = (total_g)//(r*c)
        avg_b = (total_b)//(r*c)
        for i in range(r):
            for j in range(c):
                if (rows//scale_factor) < scaled_mat.shape[0] and (columns//scale_factor) < scaled_mat.shape[1]:
                    scaled_mat[rows//scale_factor][columns//scale_factor] = [avg_r, avg_g, avg_b]
        return

    r = r//2
    c = c//2 
    #if each element is not the same, then the section is divided into 4
    topleft = quad_tree(matrix,r,c,rows,columns,threshold,scaled_mat,scale_factor)
    topright = quad_tree(matrix,r,c,rows,columns+c,threshold,scaled_mat,scale_factor)
    bottomleft = quad_tree(matrix,r,c,rows+r,columns,threshold,scaled_mat,scale_factor)
    bottomright = quad_tree(matrix,r,c,rows+r,columns+c,threshold,scaled_mat,scale_factor)

# # matrix initialization
# mat_size = 32  # works with any multiple of 4
# matrix = def_mat(mat_size,mat_size)

# # original image visualization
# show(matrix, "Original")

# # scaled matrix initialization
# scale_factor = 4
# scaled_matrix = np.zeros((mat_size//scale_factor, mat_size//scale_factor))

# # scaled matrix visualization
# quad_tree(matrix, 512, 512, 0, 0, 40, scaled_matrix, scale_factor)
# show(scaled_matrix, "Downscaled Matrix")

# image initialization & visualization
img_ad = r"Images\\city.jpeg"
img = read(img_ad)
show(img, "Original Image")

# scaled image matrix initialization
scale_factor = 4
scaled_image = create_out_mat(img.shape[0]//scale_factor, img.shape[1]//scale_factor)

# scaled image visualization
quad_tree(img, img.shape[0], img.shape[1], 0, 0, 40, scaled_image, scale_factor)
show(scaled_image, "Scaled image")