

from PIL import Image

def read_image(image_path):
    return Image.open(image_path)

def get_dominant_colour(matrix):
    colour_count = {}
    for row in matrix:
        for pixel in row:
            if pixel in colour_count:
                colour_count[pixel] += 1
            else:
                colour_count[pixel] = 1
    # print(colour_count)
    dominant_colour = max(colour_count, key=colour_count.get)
    return dominant_colour

def create_tinted_image(image_path, tint_factor=0.2):
    img = read_image(image_path)
    pixels = img.load()

    width, height = img.size
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

    input_colour = input("Enter a colour to tint the image [red/blue/green/dominant]:  ")
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    dominant_colour=()
    if input_colour=='red':
        dominant_colour=red
    elif input_colour=='green':
        dominant_colour=green
    elif input_colour=='blue':
        dominant_colour=blue
    elif input_colour=='dominant':
        dominant_colour= get_dominant_colour(matrix)
    

    quad_tree(matrix, width, height, 0, 0, dominant_colour, pixels, tint_factor)
    
    img.show()
    return img

def quad_tree(matrix, rows, cols, row, column, dominant_colour, pixels, tint_factor):
    img= read_image(image_path)
    

    if rows == 1 and cols == 1:  # terminate recursion if the quadrant size is too small
       
        original_color = pixels[row, column]
        tinted_color = (
              min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255)
        )
        pixels[row, column] = tinted_color
        return
    elif rows == 1:
        
        
        
        for j in range(0,cols):
            original_color = pixels[row, column+j]
            tinted_color = (
            min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255))
         
            pixels[row, column+j] = tinted_color
            
        return
    elif cols == 1:
        
        for i in range(0,rows):
            original_color = pixels[row+i, column]
            tinted_color = (
            min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255))
         
            pixels[row+i, column] = tinted_color
            
        return



    
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    quad_tree(matrix, half_r, half_c, row, column, dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r, half_c + extra_c, row, column + half_c, dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r + extra_r, half_c, row + half_r, column,dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, dominant_colour, pixels, tint_factor)





            
image_path = r"Images\\colour.jpg"
original = read_image(image_path)
original.show()
print(create_tinted_image(image_path))

tinted_image = create_tinted_image(image_path)
tinted_image.show()
