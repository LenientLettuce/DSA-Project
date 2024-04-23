from PIL import Image

def read_image(image_path):
    return Image.open(image_path)

def calculate_gray_value(value):
    # calculate grayscale value using the luminosity method
    return int(0.2989 * value + 0.5870 * value + 0.1140 * value)

#calls on the quad tree function and creates the grayscale image
def convert_to_grayscale(image_path):
    img = Image.open(image_path)

    pixels = img.load()
    print(pixels)
    width, height = img.size

    matrix = [[pixels[x, y][0] for x in range(width)] for y in range(height)]

    quad_tree(matrix, width, height, 0, 0, pixels)

    return img

def quad_tree(matrix, rows, cols, row, column, pixels):
   
    
    if rows == 1 and cols == 1:
        original_color = pixels[row, column]
        gray_value = calculate_gray_value(original_color[0])  # assuming grayscale is in the first channel
        pixels[row, column] = (gray_value, gray_value, gray_value)  # set RGB values for grayscale
        return
    
    elif rows == 1:
        
        for i in range(0,cols):
            original_color = pixels[row, column+i]
            gray_value = calculate_gray_value(original_color[0])
            pixels[row, column+i] = (gray_value, gray_value, gray_value)
        return
    elif cols == 1:
        
        for j in range(0,rows):
            original_color = pixels[row+j, column]
            gray_value = calculate_gray_value(original_color[0])
            pixels[row+j, column] = (gray_value, gray_value, gray_value)
        return
    
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    quad_tree(matrix, half_r, half_c, row, column, pixels)

    quad_tree(matrix, half_r, half_c + extra_c, row, column + half_c,pixels)

    quad_tree(matrix, half_r + extra_r, half_c, row + half_r, column, pixels)

    quad_tree(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, pixels)


            
image_path = r"nature.jpg"
original = read_image(image_path)
original.show()

grayscale = convert_to_grayscale(image_path)
grayscale.show()
