from PIL import Image

def read_image(image_path):
    # Open and read the image from the specified path
    return Image.open(image_path)

def show_image(image, title="Image"):
    # Show the image with the specified title
    image.show(title)

def save_image(image, output_path):
    # Save the image to the specified output path
    image.save(output_path)

def calculate_gray_value(min_val, max_val):
    # Calculate the grayscale value based on the range of pixel values in the quadrant
    return (min_val + max_val) // 2  # Simple average of min and max values

def quad_tree(matrix, n, rows, columns):
    if rows >= len(matrix) or columns >= len(matrix[0]) or rows + 1 >= len(matrix) or columns + 1 >= len(matrix[0]):
        # Check if the row or column is out of bounds
        return None

    if n <= 1:
        # Calculate grayscale value based on the range of pixel values in the quadrant
        min_val = min(matrix[rows][columns], matrix[rows + 1][columns], matrix[rows][columns + 1], matrix[rows + 1][columns + 1])
        max_val = max(matrix[rows][columns], matrix[rows + 1][columns], matrix[rows][columns + 1], matrix[rows + 1][columns + 1])
        gray_value = calculate_gray_value(min_val, max_val)

        # Set grayscale value for the quadrant
        matrix[rows][columns] = gray_value
        matrix[rows + 1][columns] = gray_value
        matrix[rows][columns + 1] = gray_value
        matrix[rows + 1][columns + 1] = gray_value
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
        return

    n = n // 2
    quad_tree(matrix, n, rows, columns)
    quad_tree(matrix, n, rows, columns + n)
    quad_tree(matrix, n, rows + n, columns)
    quad_tree(matrix, n, rows + n, columns + n)

def convert_to_grayscale(image_path):
    # Read the image and load its pixels
    img = read_image(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Create a matrix from the pixel values of the image
    matrix = [[pixels[x, y][0] for x in range(width)] for y in range(height)]

    # Apply quadtree algorithm to convert regions to grayscale
    quad_tree(matrix, width, 0, 0)

    # Update the image pixels with the grayscale values
    for y in range(height):
        for x in range(width):
            pixels[x, y] = (matrix[y][x], matrix[y][x], matrix[y][x])  # Set red, green, and blue channels to the grayscale value

    return img

# Specify the path to the image
image_path = r"flower.jpg"
img=read_image(image_path)
show_image(img)
# Convert the image to grayscale using quadtree algorithm
gray_image = convert_to_grayscale(image_path)

# Show the grayscale image
show_image(gray_image, "Grayscale Image")