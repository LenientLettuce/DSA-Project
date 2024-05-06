from PIL import Image
from helper import*

def read_image(image_path):
    return Image.open(image_path)

def calculate_gray_value(value):
    # Calculate grayscale value using the luminosity method using all the RGB channels
    return int(0.2989 * value[0] + 0.5870 * value[1] + 0.1140 * value[2])


def convert_to_grayscale(image_path):
    img = Image.open(image_path)
    pixels = img.load()              #gets all the RGB values in tuples from the image
    width, height = img.size

    # Create a matrix to store RGB values
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matrix.append(row)
    
    
    # Process the matrix using quad tree to convert RGB to grayscale
    gray_scale(matrix, height, width, 0, 0)

    # Create a new image from the modified matrix
    output_img = Image.new("RGB", (width, height))
    output_pixels = output_img.load()

    for row in range(height):
        for col in range(width):
            output_pixels[col, row] = matrix[row][col]

    return output_img


def gray_scale(matrix, rows, cols, row, column):
   
    
    if rows == 1 and cols == 1:
        original_color = matrix[row][column]
        gray_value = calculate_gray_value(original_color) 
        matrix[row][column] = (gray_value, gray_value, gray_value)  # Set RGB values for grayscale
        return
    
    elif rows == 1:
        
        for i in range(0,cols):
            original_color = matrix[row][column+i]
            gray_value = calculate_gray_value(original_color)
            matrix[row][column+i] = (gray_value, gray_value, gray_value)
        return
    elif cols == 1:
        
        for j in range(0,rows):
            original_color = matrix[row+j][column]
            gray_value = calculate_gray_value(original_color)
            matrix[row+j][column] = (gray_value, gray_value, gray_value)
        return
    
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    gray_scale(matrix, half_r, half_c, row, column)

    gray_scale(matrix, half_r, half_c + extra_c, row, column + half_c)

    gray_scale(matrix, half_r + extra_r, half_c, row + half_r, column)

    gray_scale(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c)


def main(image):
    image_path = f"Images\\{image}"
    #show original image
    #original = read_image(image_path)
    # original.show()
    #show grayscale image
    grayscale = convert_to_grayscale(image_path)
    grayscale.show()

# main(image_path="")
