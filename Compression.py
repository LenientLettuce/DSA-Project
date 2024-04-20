import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *

def full_comp(matrix, r, c, row, column,threshold,output_matrix):
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
    half_c = c // 2
    extra_c = c % 2
    topleft = full_comp(matrix, half_r, half_c, row, column,threshold,output_matrix)
    topright = full_comp(matrix, half_r, half_c + extra_c, row, column + half_c,threshold,output_matrix)
    bottomleft = full_comp(matrix, half_r + extra_r, half_c, row + half_r, column,threshold,output_matrix)
    bottomright = full_comp(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,threshold,output_matrix)
    return

def depth_compression(matrix, r, c, row, column,depth,req_depth,output_matrix):
    if depth == req_depth:
        total = [0,0,0]
        for i in range(r):
            for j in range(c):
                for k in range(0,3):
                    try:
                        total[k] += matrix[row + i][column + j][k]
                    except:
                        pass

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
    half_c = c // 2
    extra_c = c % 2
    topleft = depth_compression(matrix, half_r, half_c, row, column,depth+1,req_depth,output_matrix)
    topright = depth_compression(matrix, half_r, half_c + extra_c, row, column + half_c,depth+1,req_depth,output_matrix)
    bottomleft = depth_compression(matrix, half_r + extra_r, half_c, row + half_r, column,depth+1,req_depth,output_matrix)
    bottomright = depth_compression(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,depth+1,req_depth,output_matrix)
    return

        
def mainf(image):
    img= read(image)
    shape = (img.shape)
    print("Image Imported")

    r = shape[0] #Getting the dimensions of the image
    c = shape[1]
    rows = 0
    columns = 0
    stregth = 25
    threshold = [stregth,stregth,stregth]
    output_matrix = create_out_mat(r,c) #Creating the matrix which will eventually become the
                                        #compressed image
    print("Output Matrix Created")
    print("Compressing Image")
    full_comp(img,r,c,rows,columns,threshold,output_matrix)
    print("Image Compressed")

    print("Saving Compressed Image")
    name = "Compressed8K"
    conv_mat_img(output_matrix,name)#converting output matrix to image and saving it
    print("Complete")

def maind(image):
    img= read(image)
    shape = (img.shape)
    print("Image Imported")

    r = shape[0] #Getting the dimensions of the image
    c = shape[1]
    rows = 0
    columns = 0
    gif = []
    output_matrix = create_out_mat(r,c) #Creating the matrix which will eventually become the
                                        #compressed image
    print("Output Matrix Created")
    print("Compressing Image")
    for i in range(0,9):
        depth_compression(img,r,c,rows,columns,0,i,output_matrix)
        image = Image.fromarray(output_matrix, mode="RGB")
        image.save("Images\\Gif\\City" + str(i) + ".jpg")
        gif.append(image)

    create_gif(gif, "Images\\Gif\\City")  
    print("Complete")

def create_gif(images,name):
    first = images[0]
    first.save(name + ".gif",format = "GIF", append_images = images, save_all = True, duration = 300, loop = 1)

maind(r"Images\\city.jpeg")