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

    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matrix.append(row)
    
    

    # Process the matrix using quad tree to convert RGB to grayscale
    img_comp(matrix, height, width, 0, 0, contrast_factor)

    # Create a new image from the modified matrix
    output_img = Image.new("RGB", (width, height))
    output_pixels = output_img.load()

    for row in range(height):
        for col in range(width):
            output_pixels[col, row] = matrix[row][col]

    return output_img

# quad tree function to apply contrast 
def img_comp(matrix, rows, cols, row, column, contrast_factor):
    # base case: terminate recursion if the quadrant size is too small
    if rows == 1 and cols == 1:
        original_color = matrix[row][column]      #accessing pixels in the row and column
        adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)  #the set way to increase contrast
        matrix[row][column] = adjusted_color          #replacing pixels w the new adjusted values
        return
    elif rows == 1:  # if only one row in the quadrant
        for j in range(cols):
            original_color = matrix[row][column + j]
            adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)
            matrix[row][column + j] = adjusted_color
        return
    elif cols == 1:  # if only one column in the quadrant
        for i in range(rows):
            original_color = matrix[row + i][column]
            adjusted_color = tuple(int((c - 128) * contrast_factor + 128) for c in original_color)
            matrix[row + i][column] = adjusted_color
        return

    # divide the quadrant into sub-quadrants
    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    
    # apply contrast  recursively to each sub-quadrant
    img_comp(matrix, half_r, half_c, row, column, contrast_factor)
    img_comp(matrix, half_r, half_c + extra_c, row, column + half_c, contrast_factor)
    img_comp(matrix, half_r + extra_r, half_c, row + half_r, column, contrast_factor)
    img_comp(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c, contrast_factor)


def main(image,contrast_factor):
    # image file path
    image_path = f"Images\\{image}"
    contrast_image = create_contrast_image(image_path, contrast_factor)
    contrast_image.show()