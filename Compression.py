import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *

def img_comp(matrix,r,c,rows,columns,threshold,output_matrix):
    allsame = True
    total = [0,0,0]
    if r == 1 or c == 1: #Means one dimension of image is only single pixel
        if r <= 1 and c <= 1:
            output_matrix[rows][columns] = matrix[rows][columns]
        elif r <= 1:
            for j in range(c):
                for k in range(0,3):
                            total[k] += matrix[rows][columns + j][k]
                            if abs(int(matrix[rows][columns][k]) - int(matrix[rows][columns + j][k])) > threshold[k]:
                                allsame = False
                                break

            if allsame:
                for k in range(0,3):
                    total[k] = total[k]//c
                for j in range(c):
                    output_matrix[rows][columns+j] = total
            else:
                for j in range(c):
                    output_matrix[rows][columns+j] = matrix[rows][columns+j]
            
        elif c <= 1:
            for i in range(r):
                for k in range(0,3):
                            total[k] += matrix[rows + i][columns][k]
                            if abs(int(matrix[rows][columns][k]) - int(matrix[rows + i][columns][k])) > threshold[k]:
                                allsame = False
                                break

            if allsame:
                for k in range(0,3):
                    total[k] = total[k]//r
                for i in range(r):
                    output_matrix[rows+i][columns] = total
            else:
                for i in range(r):
                    output_matrix[rows+i][columns] = matrix[rows+i][columns]
        return
    
    for i in range(r): #Code to check if all pixels in img are within certain threshold
        if allsame == True:
            for j in range(c):
                if allsame == True:
                    for k in range(0,3):
                            total[k] += matrix[rows + i][columns + j][k]
                            if abs(int(matrix[rows][columns][k]) - int(matrix[rows + i][columns + j][k])) > threshold[k]:
                                allsame = False
                                break
                else:
                    break
        else:
            break
    
    if allsame: #if they are, it avg their value
        for k in range(0,3):
            try:
                total[k] = total[k]//(r*c)
            except:
                total[k] = total[k]
        for i in range(r):
            for j in range(c):
                for k in range (3):
                    output_matrix[rows + i][columns + j][k] = np.uint8(math.floor(total[k]))
        return
    

    r = (r)//2
    c = (c)//2
    topleft = img_comp(matrix,r,c,rows,columns,threshold,output_matrix)
    topright = img_comp(matrix,r,c,rows,columns + c,threshold,output_matrix)
    bottomleft = img_comp(matrix,r,c,rows + r,columns,threshold,output_matrix)
    bottomright = img_comp(matrix,r,c,rows + r,columns + c,threshold,output_matrix)

def new_comp(matrix, r, c, row, column,threshold,output_matrix):
    # Base case: if the matrix is 1x1, 1xc, or rx1, return the value at the current position
    total = [0,0,0]
    if r == 1 and c == 1:
        try:
            output_matrix[row][column] = matrix[row][column]
        except:
            pass
        return
    elif r == 1:
        for j in range(0,c):
            try:
                output_matrix[row][column+j] = matrix[row][column+j]
            except:
                pass
        return
    elif c == 1:
        for i in range(0,r):
            try:
                output_matrix[row+i][column] = matrix[row+i][column]
            except:
                pass
        return

    allSame = True
    for i in range(r):
        for j in range(c):
            for k in range(0,3):
                try:
                    total[k] += matrix[row + i][column + j][k]
                    if abs(int(matrix[row][column][k]) - int(matrix[row + i][column + j][k])) > threshold[k]:
                        allSame = False
                        break
                except:
                    pass

    if allSame:
        try:
            for k in range(0,3):
                total[k] = np.uint8(total[k]//(r*c))
            for i in range(r):
                for j in range(c):
                    output_matrix[row + i][column + j] = total
        except:
            pass
        return
    
    half_r = r // 2
    extra_r = r % 2
    half_r = half_r + extra_r
    half_c = c // 2
    extra_c = c % 2
    half_c = half_c + extra_c
    topleft = new_comp(matrix, half_r, half_c, row, column,threshold,output_matrix)
    topright = new_comp(matrix, half_r, half_c, row, column + half_c,threshold,output_matrix)
    bottomleft = new_comp(matrix, half_r, half_c, row + half_r, column,threshold,output_matrix)
    bottomright = new_comp(matrix, half_r, half_c, row + half_r, column + half_c,threshold,output_matrix)
    return

        
def main(image):
    img= read(image)
    shape = (img.shape)
    print("Image Imported")

    r = shape[0] #Getting the dimensions of the image
    c = shape[1]
    rows = 0
    columns = 0
    threshold = [25,25,25]
    output_matrix = create_out_mat(r,c) #Creating the matrix which will eventually become the
                                        #compressed image
    print("Output Matrix Created")
    print("Compressing Image")
    new_comp(img,r,c,rows,columns,threshold,output_matrix)
    print("Image Compressed")

    print("Saving Compressed Image")
    name = "Compressedflower"
    conv_mat_img(output_matrix,name)#converting output matrix to image and saving it
    print("Complete")

main(r"Images\\flower.jpg")