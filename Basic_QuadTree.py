import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *


def quad_tree(matrix,r,c,rows,columns,threshold): #Basic QuadTree Function
    if r <= 1 or c <= 1: #Means one or more dimension/s of image is only single hence image cannot be divided into 4
        if r <= 1 and c <= 1: #means both dimensions are only single pixels
            pass
        elif r <= 1: #means rows are single pixel
            pass    
        elif c <= 1: #means columns are single pixel
            pass
        return
    allsame = True
    total = 0
    for i in range(r): #Loop checks whether each element within the quad tree is same or not
        if allsame == True:
            for j in range(c):
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
                matrix[rows + i][columns + j] = avg
        return

    r = r//2
    c = c//2 
    #if each element is not the same, then the section is divided into 4
    topleft = quad_tree(matrix,r,c,rows,columns,threshold)
    topright = quad_tree(matrix,r,c,rows,columns+c,threshold)
    bottomleft = quad_tree(matrix,r,c,rows+r,columns,threshold)
    bottomright = quad_tree(matrix,r,c,rows+r,columns+c,threshold)

def new_quad(matrix, rows, cols, row, column,threshold):
    # Base case: if the matrix is 1x1, 1xc, or rx1, return the value at the current position
    if rows == 1 and cols == 1:
        return
    elif rows == 1:
        for j in range(0,cols):
            pass
        return
    elif cols == 1:
        for i in range(0,rows):
            pass
        return

    allSame = True
    total = 0
    for i in range(rows):
        for j in range(cols):
            total += matrix[row + i][column + j]
            if abs(matrix[row][column] - matrix[row + i][column + j]) > threshold:
                allSame = False
                break

    if allSame:
        avg = (total)//(row*column)
        for i in range(rows):
            for j in range(cols):
                matrix[row + i][column + j] = avg
        return
    
    half_rows = rows // 2
    half_cols = cols // 2
    topleft = new_quad(matrix, half_rows, half_cols, row, column,threshold)
    topright = new_quad(matrix, half_rows, half_cols, row, column + half_cols,threshold)
    bottomleft = new_quad(matrix, half_rows, half_cols, row + half_rows, column,threshold)
    bottomright = new_quad(matrix, half_rows, half_cols, row + half_rows, column + half_cols,threshold)
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