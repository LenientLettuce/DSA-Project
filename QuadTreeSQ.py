import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math
from PIL import Image

def read(filename):
    img = plt.imread(filename)
    return img

def show(img,title):
    plt.imshow(img)
    plt.title(title)
    plt.show()

def def_mat (r,c):
    output = np.random.randint(100, size=(r,c))
    return output

def create_out_mat(r,c): #Creates a 3D matrix which stores RGB Values
    output = np.zeros((r,c,3),dtype=np.uint8)
    return output

def conv_mat_img(image_data):
    image = Image.fromarray(image_data, mode="RGB")
    image.save("CompressedImage.jpg")

def img_comp(matrix,r,c,rows,columns,threshold,output_matrix):
    allsame = True
    total = [0,0,0]
    if r <= 1 and c <= 1: #Means image is only single pixel
        output_matrix[rows + r][columns + c] = matrix[rows + r][columns + c]
        return
    if r <= 1: #Ensures recursion doesn't stop until both rows and columns are compressed
        r = 2
    if c <= 1:
        c = 2
    for i in range(r): #Code to check if all pixels in img are within certain threshold
        if allsame == True:
            for j in range(c):
                if allsame == True:
                    for k in range(0,3):
                        total[k] += matrix[rows + i][columns + j][k]
                        if abs(int(matrix[rows][columns][k]) - int(matrix[rows + i][columns + j][k])) > threshold[k]:
                            allsame = False
                            break
                else:
                    break
        else:
            break
    
    if allsame: #if they are, it avg their value
        for k in range(0,3):
            total[k] = total[k]//(r*c)
        for i in range(r):
            for j in range(c):
                for k in range (3):
                    output_matrix[rows + i][columns + j][k] = np.uint8(math.floor(total[k]))
        return
    
    r = r//2
    c = c//2

    topleft = img_comp(matrix,r,c,rows,columns,threshold,output_matrix)
    topright = img_comp(matrix,r,c,rows,columns+c,threshold,output_matrix)
    bottomleft = img_comp(matrix,r,c,rows+r,columns,threshold,output_matrix)
    bottomright = img_comp(matrix,r,c,rows+r,columns+c,threshold,output_matrix)

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

def main(image):
    img= read(image)
    shape = (img.shape)
    print("Image Imported")

    r = shape[0] #Getting the dimensions of the image
    c = shape[1]
    rows = 0
    columns = 0
    threshold = [25,25,25]
    output_matrix = create_out_mat(r,c) #Creating the matrix which will eventually become the
                                        #compressed image
    print("Output Matrix Created")
    print("Compressing Image")
    img_comp(img,r,c,rows,columns,threshold,output_matrix)
    print("Image Compressed")

    print("Saving Compressed Image")
    conv_mat_img(output_matrix)#converting output matrix to image and saving it
    print("Complete")

def test_diff_aspect():
    r = [4,3,1,16,5,5,3,2,1,9,3,5]
    c = [3,2,1,9,3,5,4,3,1,16,5,5]

    for i in range(len(r)):
        matrix = def_mat(r[i],c[i])
        show(matrix, "og")
        quad_tree(matrix,r[i],c[i],0,0,50)
        show(matrix, "comp")

image=r"dsa_proj\\flower.jpg"
#image=r"Smoll.jpg"
main(image)
#test_diff_aspect()
