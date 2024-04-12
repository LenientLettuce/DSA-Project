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

def conv_mat_img(image_data,name):
    image = Image.fromarray(image_data, mode="RGB")
    image.save("Images\\" + name + ".jpg")

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

def create_custom_img(r,c):
    image_data = np.random.randint(255, size=(r,c,3))
    image = Image.fromarray(image_data, mode="RGB")
    image.save("Images\\Custom.jpg")

def weighted_average(hist):
    """Returns the weighted color average and error from a hisogram of pixles"""
    total = sum(hist)
    value, error = 0, 0
    if total > 0:
        value = sum(i * x for i, x in enumerate(hist)) / total
        error = sum(x * (value - i) ** 2 for i, x in enumerate(hist)) / total
        error = error ** 0.5
    return value, error


def color_from_histogram(hist):
    """Returns the average rgb color from a given histogram of pixle color counts"""
    r, re = weighted_average(hist[:256])
    g, ge = weighted_average(hist[256:512])
    b, be = weighted_average(hist[512:768])
    e = re * 0.2989 + ge * 0.5870 + be * 0.1140
    return (int(r), int(g), int(b)), e