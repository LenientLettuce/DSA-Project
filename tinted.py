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

    # r = r // 2
    # c = c // 2
    # # If each element is not the same, then the section is divided into 4
    # topleft = quad_tree(matrix, r, c, rows, columns, threshold)
    # topright = quad_tree(matrix, r, c, rows, columns + c, threshold)
    # bottomleft = quad_tree(matrix, r, c, rows + r, columns, threshold)
    # bottomright = quad_tree(matrix, r, c, rows + r, columns + c, threshold)
    half_r = r // 2
    extra_r = r % 2
    half_c = c // 2
    extra_c = c % 2
    topleft= quad_tree(matrix, half_r, half_c, rows, columns,threshold)
    bottomleft=quad_tree(matrix, half_r, half_c + extra_c, rows, columns + half_c,threshold)
    topright=quad_tree(matrix, half_r + extra_r, half_c, rows + half_r, columns,threshold)
    bottomright=quad_tree(matrix, half_r + extra_r, half_c + extra_c, rows + half_r, columns + half_c,threshold)

    if topleft == topright == bottomleft == bottomright:
        return topleft
    else:
        return None


def create_tinted_image(image_path, threshold=10, tint_factor=0.6):
    img = read_image(image_path)
    pixels = img.load()

    width, height = img.size
    matrix = [[pixels[x, y] for x in range(width)] for y in range(height)]

    dominant_color = get_dominant_color(matrix)
    quad_tree(matrix, width, height, 0, 0, threshold)
    
    for y in range(height):
        for x in range(width):
            original_color = pixels[x, y]
            
            tinted_color = (
                min(int(original_color[0] + (dominant_color[0] - original_color[0]) * tint_factor), 255),
                min(int(original_color[1] + (dominant_color[1] - original_color[1]) * tint_factor), 255),
                min(int(original_color[2] + (dominant_color[2] - original_color[2]) * tint_factor), 255)
            )
            pixels[x, y] = tinted_color
           
    return img

# Example usage
image_path = r"galaxy.jpg"
original_image = read_image(image_path)
original_image.show()

tinted_image = create_tinted_image(image_path)
tinted_image.show()


