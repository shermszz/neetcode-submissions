class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            You want to return the items inside the matrix from top left all the way down into the middle in a clockwise manner
            The matrix now has m rows and n columns, not necessarily a square matrix anymore
            We need to use left, right, top and bottom pointers.

            We maintain a result list and always append to it as we move 
            The general flow:
                - We have 4 fixed pointers at the start, left, right = 0, cols - 1 and top, bottom = 0, rows - 1
                - Then, we will have a curr pointer that will be tracking every word we are readin

                - We start with top left, and we will travel across the TOP row
                - We read matrix[top][curr + i] until we hit right pointer.
                - Once hit right pointer, we are done with the top row, so we do top += 1

                - Next, we travel on the RIGHT column downwards.
                - We read matrix[curr + i][right] until we hit the bottom pointer
                - Once hit the bottom poitner, we are done with that right most column, do right -= 1

                - Next we travel on the BOTTOM row across to the left
                - We read matrix[bottom][curr - i] until we hit the left pointer
                - Once hit the left pointer, we are done with that bottom row, do bottom -= 1

                - Next, we travel on the LEFT row upwards
                - We read matrix[curr - i][left] until we hit the top pointer
                - Once hit the top pointer, we are done with the left row
            We stop only once l > r or b > t

        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1
        res = []
        while left <= right and top <= bottom:
            # First, we flow the top row until we hit the right pointer
            for i in range(left, right + 1): # We read the entire row
                res.append(matrix[top][i])
            top += 1

            # next, we flow from the right column down until we hit the bottom pointer
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Because it is a rectangle matrix, we need to check if the boundaries have crossed
            if top > bottom or left > right:
                break

            # Next, we flow the bottom row from right to left until we hit the left pointer
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # Lastly, we flow upwards the left column until we hit the top pointer
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
