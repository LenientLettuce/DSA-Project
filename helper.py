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

def read_image(image_path):
    return Image.open(image_path)

def get_dominant_color(matrix):
    color_count = {}
    for row in matrix:
        for pixel in row:
            if pixel in color_count:
                color_count[pixel] += 1
            else:
                color_count[pixel] = 1

    dominant_color = max(color_count, key=color_count.get)
    return dominant_color

def read_image(image_path):
    # Open and read the image from the specified path
    return Image.open(image_path)

def show_image(image, title="Image"):
    # Show the image with the specified title
    image.show(title)

def save_image(image, output_path):
    # Save the image to the specified output path
    image.save(output_path)

def create_smoll_img():
    image_data = np.array([
    [[0, 128, 255],[0, 128, 255],[0, 128, 255]],
    [[64, 192, 32],[64, 192, 32],[64, 192, 32]],
    [[100, 50, 150],[100, 50, 150],[100, 50, 150]]
    ], dtype=np.uint8)

    image = Image.fromarray(image_data, mode="RGB")
    image.save("Images\\Smoll.jpg")