import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math

def def_mat (n):
    output = np.random.randint(100, size=(n,n))
    return output

def img_comp(matrix,n,rows,columns,threshold):
    allsame = True
    total = 0
    for i in range(n):
        if allsame == True:
            for j in range(n):
                total += matrix[rows + i][columns + j]
                if abs(matrix[rows][columns] - matrix[rows + i][columns + j]) > threshold:
                    allsame = False
                    break
        else:
            break
    avg = total/n**2
    if allsame:
        for i in range(n):
            for j in range(n):
                matrix[rows + i][columns + j] = math.ceil(avg)
        return
    
    n = n//2
    topleft = img_comp(matrix,n,rows,columns,threshold)
    topright = img_comp(matrix,n,rows,columns+n,threshold)
    bottomleft = img_comp(matrix,n,rows+n,columns,threshold)
    bottomright = img_comp(matrix,n,rows+n,columns+n,threshold)

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
    topleft = quad_tree(matrix,n,rows,columns,threshold)
    topright = quad_tree(matrix,n,rows,columns+n,threshold)
    bottomleft = quad_tree(matrix,n,rows+n,columns,threshold)
    bottomright = quad_tree(matrix,n,rows+n,columns+n,threshold)



matrix = def_mat(1024)
plt.imshow(matrix, cmap="plasma")
plt.colorbar()
plt.title("Orginal Matrix Visualization")
plt.show()

for threshold_mult in range(4,11,1):
    threshold = 100 * (threshold_mult/20) #100 is the amount of unique pixels in an image
    img_comp(matrix,len(matrix),0,0,threshold)
    plt.imshow(matrix, cmap="plasma")
    plt.colorbar()
    plt.title("Edited Matrix Visualization")
    plt.show()

