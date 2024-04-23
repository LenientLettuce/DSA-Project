import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from helper import *

def rotation(matrix, r, c, row, column,output_mat,req_depth,depth=1):
    half_r = r // 2
    extra_r = r % 2
    half_c = c // 2
    extra_c = c % 2
    if depth == req_depth:
        for i in range(r):
            for j in range(c):
                try:
                    output_mat[column + j][row + i] = matrix[row + i][column + j] 
                except:
                    pass
        return
    topleft = rotation(matrix, half_r, half_c, row, column,output_mat,req_depth,depth+1)
    topright = rotation(matrix, half_r, half_c + extra_c, row, column + half_c,output_mat,req_depth,depth+1)
    bottomleft = rotation(matrix, half_r + extra_r, half_c, row + half_r, column,output_mat,req_depth,depth+1)
    bottomright = rotation(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,output_mat,req_depth,depth+1)
    
    return

# image initialization & visualization
img_ad = r"Images\\city.jpeg"
img = read(img_ad)
show(img, "Original Image")

# rotated image matrix initialization
rotated_image = create_out_mat(img.shape[1], img.shape[0])
depth = 1
#scaled image visualization
rotation(img, img.shape[0], img.shape[1], 0, 0, rotated_image, depth)
show(rotated_image, f"Rotated image, Depth: {depth}")