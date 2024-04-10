from PIL import Image

def read_image(image_path): #reads an image
    return Image.open(image_path)

def show_image(image, title="Image"):
    image.show(title)

def save_image(image, output_path):
    image.save(output_path)

def quad_tree(matrix, n, rows, columns, threshold=128):   #to check if all pixels in the quadrant are the same
    if rows >= len(matrix) or columns >= len(matrix[0]):
        return None  # checking if the row or column is out of bounds

    if n <= 1:
        # gees to every pixel, checks if it lies in the specific range, then changes to grayscale accordingly
        if 40 <= matrix[rows][columns] <= 60:
            matrix[rows][columns] = 20  # dark gray
        elif 61 <= matrix[rows][columns] <= 80:
            matrix[rows][columns] = 128  # medium gray
        elif 81 <= matrix[rows][columns] <= 100:
            matrix[rows][columns] = 220  # light gray
        elif matrix[rows][columns] >= threshold:
            if matrix[rows][columns] < 200:  # Red pixel range
                matrix[rows][columns] = 150  # Redish Gray
            else:
                matrix[rows][columns] = 255  # white
        else:
            matrix[rows][columns] = 0  # black
        return

    all_same = True
    for i in range(n):
        if not all_same:
            break
        if rows + i >= len(matrix):
            break
        for j in range(n):
            if columns + j >= len(matrix[0]):
                break
            if matrix[rows][columns] != matrix[rows + i][columns + j]:
                all_same = False
                break

    if all_same:
        if 40 <= matrix[rows][columns] <= 60:
            matrix[rows][columns] = 20  # dark Gray
        elif 61 <= matrix[rows][columns] <= 80:
            matrix[rows][columns] = 128  # medium Gray
        elif 81 <= matrix[rows][columns] <= 200:
            matrix[rows][columns] = 220  # light Gray
        elif matrix[rows][columns] >= threshold:
            if matrix[rows][columns] < 200:  # Red pixel range
                matrix[rows][columns] = 150  # Redish Gray
            else:
                matrix[rows][columns] = 255  # white
        else:
            matrix[rows][columns] = 0  # black
        return

    n = n // 2                          # reduce the quadrant size by half
    # recursively process the quadrants
    quad_tree(matrix, n, rows, columns, threshold)
    quad_tree(matrix, n, rows, columns + n, threshold)
    quad_tree(matrix, n, rows + n, columns, threshold)
    quad_tree(matrix, n, rows + n, columns + n, threshold)

def convert_to_black_white(image_path, threshold=128):
    img = read_image(image_path)
    pixels = img.load()

    # updating the image pixels with the grayscale values
    width, height = img.size
    matrix = [[pixels[x, y][0] for x in range(width)] for y in range(height)]      #creating matrix

    quad_tree(matrix, width, 0, 0, threshold)                 # quadtree procsessing

    # updating the image pixels with the grayscale values
    for y in range(height):
        for x in range(width):
            pixels[x, y] = (matrix[y][x], matrix[y][x], matrix[y][x])  # setting red green blue channels to calculate grayscale values

    return img

image_path = r"dsa_proj\\flower.jpg"
bw_image = convert_to_black_white(image_path, threshold=128)  # Set the threshold value as needed
show_image(bw_image, "Black and White Image")