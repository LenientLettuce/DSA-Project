import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math

def def_mat (n):
    output = np.random.randint(100, size=(n,n))
    return output

def quad_tree(matrix,n,rows,columns,threshold):
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
    quad_tree(matrix,len(matrix),0,0,threshold)
    plt.imshow(matrix, cmap="plasma")
    plt.colorbar()
    plt.title("Edited Matrix Visualization")
    plt.show()

