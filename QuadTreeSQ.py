import random as rand
import numpy as np
import matplotlib.pyplot as plt

def def_mat (n):
    output = np.random.randint(2, size=(n,n))
    return output

def quad_tree(matrix,n,rows,columns,depth):
    allsame = True
    for i in range(n):
        if allsame == True:
            for j in range(n):
                if matrix[rows][columns] != matrix[rows + i][columns + j]:
                    allsame = False
                    break
        else:
            break
    if allsame:
        for i in range(n):
            for j in range(n):
                matrix[rows + i][columns + j] += depth
        return
    
    n = n//2
    topleft = quad_tree(matrix,n,rows,columns,depth+1)
    topright = quad_tree(matrix,n,rows,columns+n,depth+1)
    bottomleft = quad_tree(matrix,n,rows+n,columns,depth+1)
    bottomright = quad_tree(matrix,n,rows+n,columns+n,depth+1)


matrix = def_mat(64)
plt.imshow(matrix, cmap="plasma")
plt.colorbar()
plt.title("Orginal Matrix Visualization")
plt.show()

quad_tree(matrix,len(matrix),0,0,0)
plt.imshow(matrix, cmap="plasma")
plt.colorbar()
plt.title("Edited Matrix Visualization")
plt.show()
