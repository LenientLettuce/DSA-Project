# from PIL import Image

# def read_image(image_path):
#     # Open and read the image from the specified path
#     return Image.open(image_path)

# def show_image(image, title="Image"):
#     # Show the image with the specified title
#     image.show(title)

# def save_image(image, output_path):
#     # Save the image to the specified output path
#     image.save(output_path)


# def get_dominant_color(matrix):
#     color_count = {}  # Dictionary to store count of each color

#     # Iterate through the matrix and count occurrences of each color
#     for row in matrix:
#         for pixel in row:
#             if pixel in color_count:
#                 color_count[pixel] += 1
#             else:
#                 color_count[pixel] = 1

#     # Find the color with the highest count (most dominant color)
#     dominant_color = max(color_count, key=color_count.get)
#     return dominant_color

# def quad_tree(matrix, n, rows, columns):
#     if rows >= len(matrix) or columns >= len(matrix[0]):
#         return None  # Check if the row or column is out of bounds

#     if n <= 1:
#         return matrix[rows][columns]  # Return the color value for a single pixel quadrant

#     all_same = True
#     for i in range(n):
#         if not all_same:
#             break
#         if rows + i >= len(matrix):
#             break
#         for j in range(n):
#             if columns + j >= len(matrix[0]):
#                 break
#             if matrix[rows][columns] != matrix[rows + i][columns + j]:
#                 all_same = False
#                 break

#     if all_same:
#         return matrix[rows][columns]  # Return the color value if all elements are the same

#     n = n // 2
#     topleft = quad_tree(matrix, n, rows, columns)
#     topright = quad_tree(matrix, n, rows, columns + n)
#     bottomleft = quad_tree(matrix, n, rows + n, columns)
#     bottomright = quad_tree(matrix, n, rows + n, columns + n)

#     if topleft == topright == bottomleft == bottomright:
#         return topleft
#     else:
#         return None

# def create_tinted_image(image_path):
#     img = read_image(image_path)
#     pixels = img.load()

#     width, height = img.size
#     matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

#     dominant_color = get_dominant_color(matrix)

#     for y in range(height):
#         for x in range(width):
#             r, g, b = pixels[x, y]
#             pixels[x, y] = (
#                 min(int(r + dominant_color[0] * 0.6), 255),
#                 min(int(g + dominant_color[1] * 0.6), 255),
#                 min(int(b + dominant_color[2] * 0.6), 255)
#             )

#     return img

# # Example usage
# image_path = r"colour.jpg"
# img2=read_image(image_path)
# show_image(img2)
# tinted_image = create_tinted_image(image_path)
# tinted_image.show()

from PIL import Image
from helper import *

def quad_tree(matrix, r, c, rows, columns, threshold):
    if rows >= len(matrix) or columns >= len(matrix[0]):
        return

    if r <= 1 and c <= 1:  # Means image is only a single pixel
        return

    if rows + r > len(matrix):
        r = len(matrix) - rows
    if columns + c > len(matrix[0]):
        c = len(matrix[0]) - columns

    allsame = True
    total_r, total_g, total_b = 0, 0, 0
    for i in range(r):  # Loop checks whether each element within the quad tree is the same or not
        if allsame:
            for j in range(c):
                pixel_r, pixel_g, pixel_b = matrix[rows + i][columns + j]
                total_r += pixel_r
                total_g += pixel_g
                total_b += pixel_b
                if abs(matrix[rows][columns][0] - pixel_r) > threshold:
                    allsame = False
                    break
        else:
            break

    if allsame:
        avg_r = total_r // (r * c)
        avg_g = total_g // (r * c)
        avg_b = total_b // (r * c)
        for i in range(r):
            for j in range(c):
                matrix[rows + i][columns + j] = (avg_r, avg_g, avg_b)
        return

    r = r // 2
    c = c // 2
    # If each element is not the same, then the section is divided into 4
    topleft = quad_tree(matrix, r, c, rows, columns, threshold)
    topright = quad_tree(matrix, r, c, rows, columns + c, threshold)
    bottomleft = quad_tree(matrix, r, c, rows + r, columns, threshold)
    bottomright = quad_tree(matrix, r, c, rows + r, columns + c, threshold)

    if topleft == topright == bottomleft == bottomright:
        return topleft
    else:
        return None


def create_tinted_image(image_path, threshold=10, tint_factor=0.4):
    img = read_image(image_path)
    pixels = img.load()

    width, height = img.size
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

    dominant_color = get_dominant_color(matrix)
    quad_tree(matrix, width, height, 0, 0, threshold)
    
    for y in range(height):
        for x in range(width):
            original_color = pixels[x, y]
            # img.show()
            tinted_color = (
                min(int(original_color[0] + (dominant_color[0] - original_color[0]) * tint_factor), 255),
                min(int(original_color[1] + (dominant_color[1] - original_color[1]) * tint_factor), 255),
                min(int(original_color[2] + (dominant_color[2] - original_color[2]) * tint_factor), 255)
            )
            pixels[x, y] = tinted_color
    
    return img

# Example usage
image_path = r"dsa_proj\\city.jpeg"
original_image = read_image(image_path)
original_image.show()

tinted_image = create_tinted_image(image_path)
tinted_image.show()







# from PIL import Image

# def read_image(image_path):
#     return Image.open(image_path)

# def get_dominant_color(matrix):
#     color_count = {}
#     for row in matrix:
#         for pixel in row:
#             if pixel in color_count:
#                 color_count[pixel] += 1
#             else:
#                 color_count[pixel] = 1

#     dominant_color = max(color_count, key=color_count.get)
#     return dominant_color

# def create_tinted_image(image_path, threshold=10, tint_factor=0.6):
#     img = read_image(image_path)
#     pixels = img.load()

#     width, height = img.size
#     matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

#     dominant_color = get_dominant_color(matrix)  # Calculate dominant color once
#     quad_tree(matrix, width, height, 0, 0, threshold, dominant_color, pixels, tint_factor)
    
#     img.show()
#     return img

# def quad_tree(matrix, r, c, rows, columns, threshold, dominant_color, pixels, tint_factor):
#     if r <= 1 or c <= 1:  # terminate recursion if the quadrant size is too small
#         return

#     if rows >= len(matrix) or columns >= len(matrix[0]):
#         return

#     if rows + r > len(matrix):
#         r = len(matrix) - rows
#     if columns + c > len(matrix[0]):
#         c = len(matrix[0]) - columns

#     all_same = True
#     total_r, total_g, total_b = 0, 0, 0
#     for i in range(r):  # checking if all pixels in the quadrant are similar
#         if all_same:
#             for j in range(c):
#                 pixel_r, pixel_g, pixel_b = matrix[rows + i][columns + j]
#                 total_r += pixel_r
#                 total_g += pixel_g
#                 total_b += pixel_b
#                 if abs(matrix[rows][columns][0] - pixel_r) > threshold:
#                     all_same = False
#                     break
#         else:
#             break

#     if all_same:
#         avg_r = total_r // (r * c)
#         avg_g = total_g // (r * c)
#         avg_b = total_b // (r * c)
#         for i in range(r):
#             for j in range(c):
#                 matrix[rows + i][columns + j] = (avg_r, avg_g, avg_b)
#         return

#     r = r // 2
#     c = c // 2
#     # recursively process the four quadrants
#     quad_tree(matrix, r, c, rows, columns, threshold, dominant_color, pixels, tint_factor)
#     quad_tree(matrix, r, c, rows, columns + c, threshold, dominant_color, pixels, tint_factor)
#     quad_tree(matrix, r, c, rows + r, columns, threshold, dominant_color, pixels, tint_factor)
#     quad_tree(matrix, r, c, rows + r, columns + c, threshold, dominant_color, pixels, tint_factor)

#     for y in range(rows, rows + r):
#         for x in range(columns, columns + c):
#             original_color = pixels[x, y]
#             tinted_color = (
#                 min(int(original_color[0] + (dominant_color[0] - original_color[0]) * tint_factor), 255),
#                 min(int(original_color[1] + (dominant_color[1] - original_color[1]) * tint_factor), 255),
#                 min(int(original_color[2] + (dominant_color[2] - original_color[2]) * tint_factor), 255)
#             )
#             pixels[x, y] = tinted_color

# # Example usage
# image_path = r"heart_pix_20.jpg"
# tinted_image = create_tinted_image(image_path)
# tinted_image.show()
