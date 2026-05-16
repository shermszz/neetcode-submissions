class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0]) # r = num rows, c = num columns
        left, right = 0, r * c - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            row = mid // c # Floor the value to get the row value
            col = mid % c # Mod the value to get the actual column
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # The value is on the right hand side
                left = mid + 1
            else:
                right = mid - 1
        return False


