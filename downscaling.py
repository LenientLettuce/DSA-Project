import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
import cv2
from helper import *

def new_quad(matrix, rows, cols, row, column, scaled_mat, scale_factor):
    # Base cases: if the matrix is 1x1, 1xc, or rx1, return the value at the current position
    if rows == 1 and cols == 1:
        try:
            scaled_mat[row//scale_factor][column//scale_factor] = matrix[row][column]
        except:
            pass
        return
    elif rows == 1:
        for j in range(0,cols):
            try:
                scaled_mat[row//scale_factor][(column+j)//scale_factor] = matrix[row][column+j]
            except:
                pass
        return
    elif cols == 1:
        for i in range(0,rows):
            try:
                scaled_mat[(row+i)//scale_factor][column//scale_factor] = matrix[row+i][column]
            except:
                pass
        return

    # sameness check
    allSame = True
    
    # rgb value totals
    total_r = total_g = total_b = 0
    for i in range(rows):
        for j in range(cols):
            try:
                # image shape checking
                if (row + i) < matrix.shape[0] and (column + i) < matrix.shape[1]:
                    # rgb value total incrementing
                    total_r += matrix[row + i][column + j][0]
                    total_g += matrix[row + i][column + j][1]
                    total_b += matrix[row + i][column + j][2]
                    if len(matrix[row][column]) == 1:
                        # similarity checking, very strict
                        if abs(matrix[row][column] - matrix[row + i][column + j]) > -1:
                            allSame = False
                            break
                    else:
                        total_diff = 0
                        for k in range(2):
                            # total rgb diff
                            total_diff += abs(float(matrix[row][column][k]) - float(matrix[row + i][column + j][k]))
                        # similarity checking, very strict
                        if total_diff//3 > -1:
                            allSame = False
                            break
            except:
                pass
    # downscaled pixel assigment after sameness check
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
            pass
        return
    
    # quadtree division
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    topleft = new_quad(matrix, half_r, half_c, row, column, scaled_mat, scale_factor)
    topright = new_quad(matrix, half_r, half_c + extra_c, row, column + half_c, scaled_mat, scale_factor)
    bottomleft = new_quad(matrix, half_r + extra_r, half_c, row + half_r, column, scaled_mat, scale_factor)
    bottomright = new_quad(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, scaled_mat, scale_factor)
    return


def upscale1(img_path):
    # initializing and running opencv super resolution
    image = cv2.imread(img_path, cv2.IMREAD_COLOR)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "LapSRN_x4.pb"
    sr.readModel(path)
    sr.setModel("lapsrn", 4)
    result = sr.upsample(image)
    result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
    return result

def original(filename):
    img = read(f"Images\\{filename}")
    show(img)

def main(filename, scale_factor):
    # image initialization & visualization
    img = read(f"Images\\{filename}")

    # commenting out show image for gui functionality
    # show(img)

    # scaled image matrix initialization
    scaled_image = create_out_mat(img.shape[0]//scale_factor, img.shape[1]//scale_factor)

    #scaled image visualization
    new_quad(img, img.shape[0], img.shape[1], 0, 0, scaled_image, scale_factor)

    conv_mat_img(scaled_image)
    save_img(scaled_image,"Images\\Interpolation\\downscale_test.jpg")
    downscaled_path = "Images\\Interpolation\\downscale_test.jpg"
    image = upscale1(downscaled_path)
    conv_mat_img(image)

#filename = input("What is the name of the image file you would like to use?\n")
#scale_factor = int(input("What scale_factor would you like to run? Choose 4 or 8\n"))
#if scale_factor == 4 or scale_factor == 8:
#    main(filename, scale_factor)
#else:
#   print("That is not a valid scale factor.")


# main("city.jpeg", 4)

