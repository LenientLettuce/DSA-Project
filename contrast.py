from PIL import Image

# reads image
def read_image(image_path):
    return Image.open(image_path)

# creates the contrasted image
def create_contrast_image(image_path, contrast_factor=1.5):
    
    img = read_image(image_path)
   
    pixels = img.load()       #gives access to image pixels
   
    #image dimensions
    width, height = img.size

    #matrix representation of the image using pixel values
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]
    
    #apply the contrast recursively using the quad tree function
    quad_tree(matrix, width, height, 0, 0, pixels, contrast_factor)
    
    return img

# quad tree function to apply contrast 
def quad_tree(matrix, rows, cols, row, column, pixels, contrast_factor):
    # base case: terminate recursion if the quadrant size is too small
    if rows == 1 and cols == 1:
        original_color = pixels[row, column]      #accessing pixels in the row and column
        adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)  #the set way to increase contrast
        pixels[row, column] = adjusted_color          #replacing pixels w the new adjusted values
        return
    elif rows == 1:  # if only one row in the quadrant
        for j in range(cols):
            original_color = pixels[row, column + j]
            adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)
            pixels[row, column + j] = adjusted_color
        return
    elif cols == 1:  # if only one column in the quadrant
        for i in range(rows):
            original_color = pixels[row + i, column]
            adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)
            pixels[row + i, column] = adjusted_color
        return

    # divide the quadrant into sub-quadrants
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    
    # apply contrast  recursively to each sub-quadrant
    quad_tree(matrix, half_r, half_c, row, column, pixels, contrast_factor)
    quad_tree(matrix, half_r, half_c + extra_c, row, column + half_c, pixels, contrast_factor)
    quad_tree(matrix, half_r + extra_r, half_c, row + half_r, column, pixels, contrast_factor)
    quad_tree(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, pixels, contrast_factor)



# image file path
image_path = r"colour.jpg"

# display the original image
original = read_image(image_path)
original.show()

#display the contrast-adjusted image
contrast_image = create_contrast_image(image_path, contrast_factor=1.5)
contrast_image.show()
