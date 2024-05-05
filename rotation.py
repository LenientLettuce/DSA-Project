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
    
    # quadtree call if depth not reached
    topleft = rotation(matrix, half_r, half_c, row, column,output_mat,req_depth,depth+1)
    topright = rotation(matrix, half_r, half_c + extra_c, row, column + half_c,output_mat,req_depth,depth+1)
    bottomleft = rotation(matrix, half_r + extra_r, half_c, row + half_r, column,output_mat,req_depth,depth+1)
    bottomright = rotation(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,output_mat,req_depth,depth+1)
    
    return
def main(filename, depth):
    # image initialization & visualization
    img = read(f"Images\\{filename}")
    show(img)

    # rotated image matrix initialization
    rotated_image = create_out_mat(img.shape[1], img.shape[0])
    #scaled image visualization
    rotation(img, img.shape[0], img.shape[1], 0, 0, rotated_image, depth)
    conv_mat_img(rotated_image)

    
#filename = input("What is the name of the image file you would like to use?\n")
#depth = int(input("What depth would you like to run?\n"))

#main(filename, depth)

main("city.jpeg", 1)