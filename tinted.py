
# from PIL import Image
# from helper import *

# def quad_tree(matrix, r, c, rows, columns, threshold):
#     if rows >= len(matrix) or columns >= len(matrix[0]):
#         return

#     if r <= 1 and c <= 1:  # Means image is only a single pixel
#         return

#     if rows + r > len(matrix):
#         r = len(matrix) - rows
#     if columns + c > len(matrix[0]):
#         c = len(matrix[0]) - columns

#     allsame = True
#     total_r, total_g, total_b = 0, 0, 0
#     for i in range(r):  # Loop checks whether each element within the quad tree is the same or not
#         if allsame:
#             for j in range(c):
#                 pixel_r, pixel_g, pixel_b = matrix[rows + i][columns + j]
#                 total_r += pixel_r
#                 total_g += pixel_g
#                 total_b += pixel_b
#                 if abs(matrix[rows][columns][0] - pixel_r) > threshold:
#                     allsame = False
#                     break
#         else:
#             break

#     if allsame:
#         avg_r = total_r // (r * c)
#         avg_g = total_g // (r * c)
#         avg_b = total_b // (r * c)
#         for i in range(r):
#             for j in range(c):
#                 matrix[rows + i][columns + j] = (avg_r, avg_g, avg_b)
#         return

#     r = r // 2
#     c = c // 2
#     # If each element is not the same, then the section is divided into 4
#     topleft = quad_tree(matrix, r, c, rows, columns, threshold)
#     topright = quad_tree(matrix, r, c, rows, columns + c, threshold)
#     bottomleft = quad_tree(matrix, r, c, rows + r, columns, threshold)
#     bottomright = quad_tree(matrix, r, c, rows + r, columns + c, threshold)

#     if topleft == topright == bottomleft == bottomright:
#         return topleft
#     else:
#         return None


# def create_tinted_image(image_path, threshold=10, tint_factor=0.4):
#     img = read_image(image_path)
#     pixels = img.load()

#     width, height = img.size
#     matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

#     dominant_color = get_dominant_color(matrix)
#     quad_tree(matrix, width, height, 0, 0, threshold)
    
#     for y in range(height):
#         for x in range(width):
#             original_color = pixels[x, y]
#             # img.show()
#             tinted_color = (
#                 min(int(original_color[0] + (dominant_color[0] - original_color[0]) * tint_factor), 255),
#                 min(int(original_color[1] + (dominant_color[1] - original_color[1]) * tint_factor), 255),
#                 min(int(original_color[2] + (dominant_color[2] - original_color[2]) * tint_factor), 255)
#             )
#             pixels[x, y] = tinted_color
    
#     return img

# # Example usage
# image_path = r"dsa_proj\\city.jpeg"
# original_image = read_image(image_path)
# original_image.show()

# tinted_image = create_tinted_image(image_path)
# tinted_image.show()







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




from PIL import Image

def read_image(image_path):
    return Image.open(image_path)

def get_dominant_color(matrix):
    color_count = {}
    for row in matrix:
        for pixel in row:
            if pixel in color_count:
                color_count[pixel] += 1
            else:
                color_count[pixel] = 1

    dominant_color = max(color_count, key=color_count.get)
    return dominant_color

def create_tinted_image(image_path, threshold=10, tint_factor=0.05):
    img = read_image(image_path)
    pixels = img.load()

    width, height = img.size
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

    dominant_color = get_dominant_color(matrix)  # Calculate dominant color once
    quad_tree(matrix, width, height, 0, 0, threshold, dominant_color, pixels, tint_factor)
    
    
    return img

def quad_tree(matrix, rows, cols, row, column, threshold, dominant_color, pixels, tint_factor):
    img= read_image(image_path)

    if rows == 1 and cols == 1:  # terminate recursion if the quadrant size is too small
        return
    elif rows == 1:
        for j in range(0,cols):
            try:
                pass
            except:
                pass
        return
    elif cols == 1:
        for i in range(0,rows):
            try:
                pass
            except:
                pass
        return

    if row >= len(matrix) or column >= len(matrix[0]):
        return

    if row + rows > len(matrix):
        rows = len(matrix) - row
    if column + cols > len(matrix[0]):
        cols = len(matrix[0]) - column

    all_same = True
    total_r, total_g, total_b = 0, 0, 0
    for i in range(rows):
        for j in range(cols):
            try:
                pixel_r, pixel_g, pixel_b = matrix[row + i][column + j]
                total_r += pixel_r
                total_g += pixel_g
                total_b += pixel_b
                if abs(matrix[row][column][0] - pixel_r) > threshold:
                    all_same = False
                    break
            except:
                pass

    if all_same:
        avg_r = total_r // (rows * cols)
        avg_g = total_g // (rows * cols)
        avg_b = total_b // (rows * cols)
        for i in range(rows):
            for j in range(cols):
                matrix[row + i][column + j] = (avg_r, avg_g, avg_b)
        return  # Stop further processing for this quadrant

    half_r = rows // 2
    extra_r = rows % 2
    half_c = cols // 2
    extra_c = cols % 2
    quad_tree(matrix, half_r, half_c, row, column,threshold, dominant_color, pixels, tint_factor)
    quad_tree(matrix, half_r, half_c + extra_c, row, column + half_c,threshold, dominant_color, pixels, tint_factor)
    quad_tree(matrix, half_r + extra_r, half_c, row + half_r, column,threshold, dominant_color, pixels, tint_factor)
    quad_tree(matrix, half_r + extra_r, half_c + extra_c, row + half_r, column + half_c,threshold, dominant_color, pixels, tint_factor)

    # Apply tinting only to the processed quadrant
    for y in range(row, row + rows):
        for x in range(column, column + cols):
            original_color = pixels[x, y]
            tinted_color = (
                min(int(original_color[0] + (dominant_color[0] - original_color[0]) * tint_factor), 255),
                min(int(original_color[1] + (dominant_color[1] - original_color[1]) * tint_factor), 255),
                min(int(original_color[2] + (dominant_color[2] - original_color[2]) * tint_factor), 255)
            )
            pixels[x, y] = tinted_color

            
image_path = r"colour.jpg"
original = read_image(image_path)
original.show()

tinted_image = create_tinted_image(image_path)
tinted_image.show()
