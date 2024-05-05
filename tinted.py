from PIL import Image

def read_image(image_path):
    return Image.open(image_path)

def get_dominant_colour(matrix):
    #gets dominant colour by creating a dictionary of all rgb tuples in the matrix and finding the one which has the max count
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

def create_tinted_image(image_path, threshold=10, tint_factor=0.4):
    img = read_image(image_path)
   
    pixels = img.load()       #gives access to image pixels
   
    #image dimensions
    width, height = img.size

    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matrix.append(row)
    
    

    # Process the matrix using quad tree to convert RGB to grayscale
    tinted(matrix, height, width, 0, 0, get_dominant_colour(matrix),0.5)

    # Create a new image from the modified matrix
    output_img = Image.new("RGB", (width, height))
    output_pixels = output_img.load()

    for row in range(height):
        for col in range(width):
            output_pixels[col, row] = matrix[row][col]

    return output_img

def tinted(matrix, rows, cols, row, column, dominant_colour, tint_factor):
    if rows == 1 and cols == 1:  # terminate recursion if the quadrant size is too small
       
        original_color = matrix[row][column]
        tinted_color = (
            min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),       #applies tint by accessing each integer in rgb original colour tuple and adding the dominant colur value to it , then multiplying by tint factor
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255)
        )
        matrix[row][column] = tinted_color
        return
    elif rows == 1:          #if rows==1, then making sure that all the columns are coloured
        
        
        
        for j in range(0,cols):
            original_color = matrix[row][column+j]
            tinted_color = (
            min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255))
         
            matrix[row][column+j] = tinted_color
            
        return
    elif cols == 1:
        
        for i in range(0,rows):
            original_color = matrix[row+i][column]
            tinted_color = (
            min(int(original_color[0] + (dominant_colour[0] - original_color[0]) * tint_factor), 255),
            min(int(original_color[1] + (dominant_colour[1] - original_color[1]) * tint_factor), 255),
            min(int(original_color[2] + (dominant_colour[2] - original_color[2]) * tint_factor), 255))
         
            matrix[row+i][column] = tinted_color
            
        return



    
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    tinted(matrix, half_r, half_c, row, column, dominant_colour, tint_factor)

    tinted(matrix, half_r, half_c + extra_c, row, column + half_c, dominant_colour, tint_factor)

    tinted(matrix, half_r + extra_r, half_c, row + half_r, column, dominant_colour, tint_factor)

    tinted(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, dominant_colour, tint_factor)


def main(image_path):
    image_path = r"Images\\city.jpeg"
    original = read_image(image_path)
    original.show()

    tinted_image = create_tinted_image(image_path)
    tinted_image.show()

main(image_path= "")




