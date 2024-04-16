import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from helper import *

def new_quad(matrix, rows, cols, row, column,threshold,scaled_mat,scale_factor):
    # Base case: if the matrix is 1x1, 1xc, or rx1, return the value at the current position
    if rows == 1 and cols == 1:
        try:
            pass
        except:
            pass
        return
    elif rows == 1:
        for j in range(0,cols):
            try:
                pass
            except:
                pass
        return
    elif cols == 1:
        for i in range(0,rows):
            try:
                pass
            except:
                pass
        return

    allSame = True
    total_r = total_g = total_b = 0
    for i in range(rows):
        for j in range(cols):
            try:
                if (row + i) < matrix.shape[0] and (column + i) < matrix.shape[1]:
                    total_r += matrix[row + i][column + j][0]
                    total_g += matrix[row + i][column + j][1]
                    total_b += matrix[row + i][column + j][2]
                    if len(matrix[row][column]) == 1:
                        if abs(matrix[row][column] - matrix[row + i][column + j]) > threshold:
                            allSame = False
                            break
                    else:
                        total_diff = 0
                        for k in range(2):
                            total_diff += abs(float(matrix[row][column][k]) - float(matrix[row + i][column + j][k]))
                        if total_diff//3 > threshold:
                            allSame = False
                            break
            except:
                print("exception 1")

    if allSame:
        try:
            avg_r = (total_r)//(rows*cols)
            avg_g = (total_g)//(rows*cols)
            avg_b = (total_b)//(rows*cols)
            for i in range(rows):
                for j in range(cols):
                    if (rows//scale_factor) < scaled_mat.shape[0] and (cols//scale_factor) < scaled_mat.shape[1]:
                        scaled_mat[row//scale_factor][column//scale_factor] = [avg_r, avg_g, avg_b]
        except:
            print("exception 2")
        return
    
    half_rows = (rows // 2) + (rows % 2)
    half_cols = (cols // 2) + (cols % 2)
    topleft = new_quad(matrix, half_rows, half_cols, row, column,threshold,scaled_mat,scale_factor)
    topright = new_quad(matrix, half_rows, half_cols, row, column + half_cols,threshold,scaled_mat,scale_factor)
    bottomleft = new_quad(matrix, half_rows, half_cols, row + half_rows, column,threshold,scaled_mat,scale_factor)
    bottomright = new_quad(matrix, half_rows, half_cols, row + half_rows, column + half_cols,threshold,scaled_mat,scale_factor)
    return

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
new_quad(img, img.shape[0], img.shape[1], 0, 0, 40, scaled_image, scale_factor)
show(scaled_image, "Scaled image")