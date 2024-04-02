import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from image_import import *

def def_mat (n):
    output = np.random.randint(100, size=(n,n))
    return output

def img_comp(matrix,r,c,rows,columns,threshold):
    allsame = True
    total = [0,0,0]
    for i in range(r):
        if allsame == True:
            for j in range(c):
                for k in range(total):
                    total[k] += matrix[rows + i][columns + j][k]
                    if abs(matrix[rows][columns] - matrix[rows + i][columns + j]) > threshold:
                        allsame = False
                        break
        else:
            break
    #Need to find avergae somehow
    if allsame:
        for i in range(r):
            for j in range(c):
                for k in range (total):
                    matrix[rows + i][columns + j][k] = math.ceil(total[k])
        return
    
    r = r//2
    c = c//2

    topleft = img_comp(matrix,r,c,rows,columns,threshold)
    topright = img_comp(matrix,r,c,rows,columns+c,threshold)
    bottomleft = img_comp(matrix,r,c,rows+r,columns,threshold)
    bottomright = img_comp(matrix,r,c,rows+r,columns+c,threshold)

def quad_tree(matrix,n,rows,columns): #Basic QuadTree Function
    allsame = True
    for i in range(n): #Loop checks whether each element within the quad tree is same or not
        if allsame == True:
            for j in range(n):
                if abs(matrix[rows][columns] != matrix[rows + i][columns + j]):
                    allsame = False
                    break
        else:
            break

    if allsame: #if each element is same, then the section is kept as is
        return

    n = n//2 #if each element is not the same, then the section is divided into 4
    topleft = quad_tree(matrix,n,rows,columns)
    topright = quad_tree(matrix,n,rows,columns+n)
    bottomleft = quad_tree(matrix,n,rows+n,columns)
    bottomright = quad_tree(matrix,n,rows+n,columns+n)

image=r"dsa_proj\\8kimg.jpg"
img= read(image)
show(img,"Original")

print(img)

#for threshold_mult in range(4,11,1):
#    threshold = 100 * (threshold_mult/20) #100 is the amount of unique pixels in an image
#    img_comp(matrix,len(matrix),0,0,threshold)
#    plt.imshow(matrix, cmap="plasma")
#    plt.colorbar()
#    plt.title("Edited Matrix Visualization")
#    plt.show()

