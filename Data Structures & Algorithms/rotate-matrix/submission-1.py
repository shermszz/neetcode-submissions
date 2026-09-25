class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        GOAL: Rotate all the values clockwise (right -> left) by 90 degrees.
            - We want to rotate the whole box basically and bring each number along the rotation
        
        A general pattern:
            - Top left --> Top right
            - Top right --> Bottom right
            - Bottom right --> Bottom left
            - Bottom left --> Top left
            For the elements not at the corners, how do they move?
            
        
        Lets say we have a 3 * 3 matrix
            - [0][0] --> [0][2] right side +2 
            - [0][2] --> [2][2] left side + 2 
            - [2][2] --> [2][0] right side - 2
            - [2][0] --> [0][0] left side -2

        (HAD TO WATCH THE SOLUTION BREAKDOWN TO ATTEMPT, reattempt again this question)
            The pattern is that we will have left and right pointers to start. 
            We will work our way from outer square all the way down to the inner square.
            Once we have our boundaries set, we will do the rotation in REVERSE order so that we just need one temporary variable to track what needs to be swapped.
            For example, we start top left using example 2
            As we iterate from left to right, we check for left < right in order to continue the execution inwards
            Then, we need to cover all the elements in that row, so we need a for loop to iterate n - 1 times
            In each loop:
                - matrix[bottom][left] should be at maxtrix[top][left].
                - We first store temp = matrix[top][left] to save that value, then we take matrix[bottom][left] and overwrite the value at matrix[top][left]
                - Then, the bottom right value should be at the bottom left, which means we simply overwrite whatever was from bottom right into bottom left (no need to store additional variables here)
                - Then, top right should be at bottom right, again just overwrite
                - finally for top right value, it should be whatever we stored in our temp variable, and we update it there
                - Once done, we shrink the bounadries of left and right first so left += 1, right -= 1 and repeat the process
        """
        n = len(matrix)
        left, right = 0, n - 1
        while left < right:
            for i in range(right - left): 
                top, bottom = left, right

                # First, we store the value of the top left value first
                # The thing is, we are iterating across the row, so we need to make sure that the value we read if the correct value
                temp = matrix[top][left + i]

                # Now, we know that the top left value should get the value at bottom left
                # The next round, we are getting the values from the row above the previous iteration, hence we get the value from bottom - i
                matrix[top][left + i] = matrix[bottom - i][left]

                # Next, the bottom left should get the value of bottom right
                # The next round we are getting the value from the left of the bottom right corner, hence we get the value from right - i
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Next, the bottom right should get the value of the top right
                # The bottom right value gets its next value from the row below 
                matrix[bottom][right - i] = matrix[top + i][right]

                # Finally, the top right gets the top left, which we stored earlier
                matrix[top + i][right] = temp
            
            left += 1
            right -= 1


