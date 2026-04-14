from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        59. Spiral Matrix II
        
        Time Complexity: O(n^2) - We iterate exactly n * n times to fill every 
        single cell in the matrix.
        Space Complexity: O(n^2) - We allocate an n x n 2D array to store the result. 
        (If the output array does not count toward auxiliary space, this is O(1)).
        """
        # Initialize an n x n matrix with 0s
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # Define the four boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        # The number we are currently inserting
        first = 1
        
        while top <= bottom and left <= right:

            # 1. Traverse from Left to Right along the Top boundary
            for c in range(left, right + 1):
                matrix[top][c] = first
                first += 1
            top += 1 # Shrink the top boundary downwards

            # 2. Traverse from Top to Bottom along the Right boundary
            for r in range(top, bottom + 1):
                matrix[r][right] = first
                first += 1
            right -= 1 # Shrink the right boundary inwards

            # 3. Traverse from Right to Left along the Bottom boundary
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c] = first
                    first += 1
                bottom -= 1 # Shrink the bottom boundary upwards

            # 4. Traverse from Bottom to Top along the Left boundary
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left] = first
                    first += 1
                left += 1 # Shrink the left boundary inwards

        return matrix