import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *


def new_quad(matrix, rows, cols, row, column,threshold):
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
    total = 0
    for i in range(rows):
        for j in range(cols):
            try:
                total += matrix[row + i][column + j]
                if abs(matrix[row][column] - matrix[row + i][column + j]) > threshold:
                    allSame = False
                    break
            except:
                pass

    if allSame:
        try:
            avg = (total)//(row*column)
            for i in range(rows):
                for j in range(cols):
                    matrix[row + i][column + j] = avg
        except:
            pass
        return
    
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    topleft = new_quad(matrix, half_r, half_c, row, column,threshold)
    topright = new_quad(matrix, half_r, half_c + extra_c, row, column + half_c,threshold)
    bottomleft = new_quad(matrix, half_r + extra_r, half_c, row + half_r, column,threshold)
    bottomright = new_quad(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,threshold)
    return



def test_diff_aspect():
    r = [4,3,1,16,5,5,3,2,1,9,3,5]
    c = [3,2,1,9,3,5,4,3,1,16,5,5]

    for i in range(len(r)):
        matrix = def_mat(r[i],c[i])
        show(matrix, "og")
        new_quad(matrix,r[i],c[i],0,0,50)
        show(matrix, "comp")

test_diff_aspect()