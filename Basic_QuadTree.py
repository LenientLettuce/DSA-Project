import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image
from helper import *


def quad_tree(matrix,r,c,rows,columns,threshold): #Basic QuadTree Function
    if r <= 1 and c <= 1: #Means image is only single pixel
        return
    if r <= 1: #Ensures recursion doesn't stop until both rows and columns are compressed
        r = 2
    if c <= 1:
        c = 2
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


def test_diff_aspect():
    r = [4,3,1,16,5,5,3,2,1,9,3,5]
    c = [3,2,1,9,3,5,4,3,1,16,5,5]

    for i in range(len(r)):
        matrix = def_mat(r[i],c[i])
        show(matrix, "og")
        quad_tree(matrix,r[i],c[i],0,0,50)
        show(matrix, "comp")