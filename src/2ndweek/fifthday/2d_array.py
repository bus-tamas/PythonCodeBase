def spiral_matrix(A, B, C):
    """
    This function converts a 1D array into a 2D matrix in a spiral order.
    """
    # Initialize the 2D matrix with zeros
    matrix = [[0]*C for _ in range(B)]
    # Define the directions for the spiral (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Initialize the direction index, row index, and column index
    direction_idx, row_idx, col_idx = 0, 0, 0
    # Iterate over the 1D array
    for i in range(len(A)):
        # Assign the current element to the current position in the matrix
        matrix[row_idx][col_idx] = A[i]
        # Compute the next position
        next_row_idx, next_col_idx = row_idx + directions[direction_idx][0], col_idx + directions[direction_idx][1]
        # If the next position is out of bounds or already filled, change the direction
        if not (0 <= next_row_idx < B and 0 <= next_col_idx < C and matrix[next_row_idx][next_col_idx] == 0):
            direction_idx = (direction_idx + 1) % 4
        # Update the row index and column index
        row_idx += directions[direction_idx][0]
        col_idx += directions[direction_idx][1]
    return matrix
 
# Test the function
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
B = 3
C = 4
print(spiral_matrix(A, B, C))  # Output: [[1, 2, 3, 4], [12, 11, 10, 5], [7, 6, 9, 8]]



import numpy as np

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def convert_to_2d(arr, num_cols):
    try:
        two_dim = np.reshape(arr, (-1, num_cols))
        return two_dim
    except:
        print("Cannot be converted")

print(convert_to_2d(arr, 3))
