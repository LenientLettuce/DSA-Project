import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *

def target(rows, cols, row, column,lst,output_matrix):
    # Base case: if the matrix is 1x1, 1xc, rx1, or has arrive at relevant quadrant change relevant values
    if rows == 1 and cols == 1:
        try:
            output_matrix[row][column] = [255,255,255]
        except:
            pass
        return
    elif rows == 1:
        for j in range(0,cols):
            try:
                output_matrix[row][column+j] = [255,255,255]
            except:
                pass
        return
    elif cols == 1:
        for i in range(0,rows):
            try:
                output_matrix[row+i][column] = [255,255,255]
            except:
                pass
        return
    elif lst == []:
        for i in range(rows):
            for j in range(cols):
                try:
                    output_matrix[row + i][column + j] = [255,255,255]
                except:
                    pass
        return

    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    if lst[0] == 1:
        topleft = target(half_r, half_c, row, column,lst[1::],output_matrix)
    if lst[0] == 2:
        topright = target(half_r, half_c + extra_c, row, column + half_c,lst[1::],output_matrix)
    if lst[0] == 3:
        bottomleft = target(half_r + extra_r, half_c, row + half_r, column,lst[1::],output_matrix)
    if lst[0] == 4:
        bottomright = target(half_r + extra_r, half_c + extra_c, row + half_r,
                              column + half_c,lst[1::],output_matrix)
    return

def write_data(output_matrix, data_matrix,r,c):
    for i in range(r):
        for j in range(c):
            try:
                output_matrix[i][j] = data_matrix[i][j]
            except:
                pass
    return

def main(image):
    #Importing Image
    img= read(image)
    shape = (img.shape)
    print("Image Imported")

    r = shape[0] #Getting the dimensions of the image
    c = shape[1]
    rows = 0
    columns = 0
    lst = []
    output_matrix = create_out_mat(r,c) #Creating the matrix which will eventually become the
                                        #compressed image
    print("Output Matrix Created")
    write_data(output_matrix, img,r,c)
    target(r,c,rows,columns,lst,output_matrix)

    print("Saving Image")
    name = "TargetCity"
    conv_mat_img(output_matrix,name)#converting output matrix to image and saving it
    print("Complete")

main(r"Images\\city.jpeg")