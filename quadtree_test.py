import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *


def new_quad(matrix, rows, cols, row, column, target, path, path_num=1):
    if rows == 1 and cols == 1:
        if matrix[row][column] == target:
            path[path_num] = [(row, column)]
            path["target"] = target
            return path
        else:
            return
    elif rows == 1:
        for j in range(cols):
            if matrix[row][column + j] == target:
                path[path_num] = [(row, column + j)]
                path["target"] = target
                return path
        return
    elif cols == 1:
        for i in range(rows):
            if matrix[row + i][column] == target:
                path[path_num] = [(row + i, column)]
                path["target"] = target
                return path
        return

    # # Commenting out old checking condition as it is only needed for functional implementation
    # allSame = True
    # total = 0
    # for i in range(rows):
    #     for j in range(cols):
    #         try:
    #             total += matrix[row + i][column + j]
    #             if abs(matrix[row][column] - matrix[row + i][column + j]) > threshold:
    #                 allSame = False
    #                 break
    #         except:
    #             pass

    # if allSame:
    #     try:
    #         avg = (total)//(row*column)
    #         for i in range(rows):
    #             for j in range(cols):
    #                 matrix[row + i][column + j] = avg
    #     except:
    #         pass
    #     return

    # Cell-Access base case
    if rows <= 2 and cols <= 2:
        for i in range(rows):
            for j in range(cols):
                if matrix[row + i][column + j] == target:
                    path[path_num] = matrix[row:row+rows][column:column+cols]
                    path["target"] = target
                    return path
    else:
        print(matrix[row:row+rows][column:column+cols])
        path[path_num] = matrix[row:row+rows][column:column+cols]
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    topleft = new_quad(matrix, half_r, half_c, row, column,target, path, path_num=1)
    topright = new_quad(matrix, half_r, half_c + extra_c, row, column + half_c,target, path, path_num=1)
    bottomleft = new_quad(matrix, half_r + extra_r, half_c, row + half_r, column,target, path, path_num=1)
    bottomright = new_quad(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,target, path, path_num=1)
    return

def init_mat(size):
    vals = [i for i in range(1, size + 1)]
    mat_size = round(64**(1/2))
    mat = [[None for i in range(mat_size)] for j in range(mat_size)]
    cur_val = 0
    for i in range(mat_size):
        for j in range(mat_size):
            mat[i][j] = vals[cur_val]
            cur_val += 1
    return mat

def main():
    mat = init_mat(64)
    # for row in mat:
    #     print(row)
    size = len(mat)
    print(new_quad(mat, size, size,0 ,0 , 63, {}))

main()
