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

def create_tinted_image(image_path, threshold=10, tint_factor=0.4):
    img = read_image(image_path)
    pixels = img.load()

    width, height = img.size
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]
    
    dominant_colour = get_dominant_colour(matrix)  #calculate dominant color once
    quad_tree(matrix, width, height, 0, 0, threshold, dominant_colour, pixels, tint_factor)
    
    
    return img

def quad_tree(matrix, rows, cols, row, column, threshold, dominant_colour, pixels, tint_factor):
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
    quad_tree(matrix, half_r, half_c, row, column,threshold, dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r, half_c + extra_c, row, column + half_c,threshold, dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r + extra_r, half_c, row + half_r, column,threshold, dominant_colour, pixels, tint_factor)

    quad_tree(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,threshold, dominant_colour, pixels, tint_factor)


            
image_path = r"city 2.jpg"
original = read_image(image_path)
original.show()

tinted_image = create_tinted_image(image_path)
tinted_image.show()





