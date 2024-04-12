import numpy as np
import matplotlib as mpl

import matplotlib.pyplot as plt
from colorthief import ColorThief


def read(filename):
    img = plt.imread(filename)
    return img

def show(img,title):
    plt.imshow(img)
    plt.title(title)
    plt.show()

image=r"dsa_proj\\dsa.jpg"

#import the image file
img=plt.imread(image)
#generates matrix
print(img.shape)

#dislay in a matplot window
fig = plt.figure()
axes = fig.subplots()
axes.imshow(img)
#black and white

plt.show()

# #change colours
def change_colours():
    #black and white
    fig = plt.figure()
    axes = fig.subplots()
    axes.imshow(img)
    f=axes.imshow(img[:, :, 1], cmap='gray', vmin=0, vmax=300)
    plt.show()
    return f
print(change_colours())

def dominant_colour():
    ct= ColorThief(image)
    dominant=ct.get_color(quality=1)
    plt.imshow([[dominant]])
    plt.show()

    palette= ct.get_palette(color_count=5)
    plt.imshow([[palette[i]for i in range(5)]])
    plt.show()

print(dominant_colour())
