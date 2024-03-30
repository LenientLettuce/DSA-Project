import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math as math

def def_mat(n):
    output = np.random.randint(100, size=(n, n))
    return output


def img_interpolate(matrix, n, rows, columns, tolerance):
    allsame = True

    for i in range(n):
        for j in range(n):
            if abs(matrix[rows][columns] - matrix[rows + i][columns + j]) > tolerance:  
                allsame = False
                break

    if allsame:
        for i in range(2 * n):
            for j in range(2 * n):
                matrix[rows + i][columns + j] = matrix[rows // 2][columns // 2]
        return

    n = n // 2
    img_interpolate(matrix, n, rows, columns, tolerance)
    img_interpolate(matrix, n, rows, columns + n, tolerance)
    img_interpolate(matrix, n, rows + n, columns, tolerance)
    img_interpolate(matrix, n, rows + n, columns + n, tolerance)

    # bilinear interpolation of boundary pixels
    for i in range(n):

        x = i / n  
        interp_value = (1 - x) * matrix[rows][columns + i] + x * matrix[rows + 2 * n][columns + i]
        matrix[rows + n][columns + i] = interp_value

        y = i / n
        interp_value = (1 - y) * matrix[rows + i][columns] + y * matrix[rows + i][columns + 2 * n]
        matrix[rows + i][columns + n] = interp_value


matrix = def_mat(250)

# original image 
plt.imshow(matrix, cmap="plasma") 
plt.colorbar()
plt.title("Original Matrix Visualization")
plt.show()

for tolerance in range(0, 40, 5):
    new_size = len(matrix) * 2
    interpolated_matrix = np.zeros((new_size, new_size), dtype=matrix.dtype)
    img_interpolate(interpolated_matrix, len(interpolated_matrix) // 2, 0, 0, tolerance)

    plt.imshow(interpolated_matrix, cmap="plasma")
    plt.colorbar()
    plt.title(f"Interpolated Image (Tolerance: {tolerance})")
    plt.show()
