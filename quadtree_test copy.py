import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *


def new_quad(matrix, rows, cols, row, column, target, path,depth = 0):
    if rows <= 2 and cols <= 2:
        count = 1
        for i in range(rows):
            for j in range(cols):
                if matrix[row + i][column + j] == target:
                    path.append([depth, count])
                    return
                else:
                    path.append([depth, count])
                    count += 1

        return
            
    
    # recursive calls
    half_r = rows // 2
    half_c = cols // 2
    path.append([depth,1])
    if target[0] >= row and target[1] >= column and target[0] < half_r and target[1] < half_c: 
        topleft = new_quad(matrix, half_r, half_c, row, column,target, path,depth + 1)
        return
    path.append([depth,2])
    if target[0] >= row and target[1] >= column + half_c and target[0] < row + half_r and target[1] < cols: 
        topright = new_quad(matrix, half_r, half_c , row, column + half_c,target, path,depth + 1)
        return
    path.append([depth,3])
    if target[0] >= row + half_r and target[1] >= 0 and target[0] < rows and target[1] < column + half_c:
        bottomleft = new_quad(matrix, half_r, half_c, row + half_r, column,target, path,depth + 1)
        return
    path.append([depth,4])
    if target[0] >= row + half_r and target[1] >= column + half_c and target[0] < rows and target[1] < cols:
        bottomright = new_quad(matrix, half_r, half_c, row + half_r, column + half_c,target, path,depth + 1)
        return

def make_mat(size):
    matrix = []
    for i in range(size):
        for j in range(size):
            matrix.append[i,j]

    return matrix


matrix = [[[0,0],[0,1],[0,2],[0,3]],
          [[1,0],[1,1],[1,2],[1,3]],
          [[2,0],[2,1],[2,2],[2,3]],
          [[3,0],[3,1],[3,2],[3,3]]]

path = []
new_quad(matrix,4,4,0,0,[2,3],path)
print(path)

            

