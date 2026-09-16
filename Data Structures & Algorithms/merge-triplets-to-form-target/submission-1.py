class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
            We have a target triplet to obtain
            inside triplets, it is an array of triplets --> We need to apply some operations here
            
            We take some triplet[i] and triplet[j]
                 - Update each one to be the maximum of both
                 - Check to see if there is a triplet where we perform this operation and we can obtain the target (return true or false)

            triplets is at least length 1
            The values are all non-negative (minimum value is 1)
            Test case 1: triplets = [[1, 2, 3], [7, 1, 1]] target = [7, 2, 3]
                - a = 7, b = 2, c = 3
                - To get this configuration, the pairs when we compare must be a <= 7, b <=2 and c <= 3
                For all triplet in triplets, as long as any of these conditions are true, we ignore them completely
                - any triplet whose a > 7 is ignored
                - any triplet whose b > 2 is ignored
                - any triplet whose c > 3 is ignored
                
                All triplets valid in this case, so we start the comparison and do it for every single triplet until we are able to form the target.
                If at the end of each operation we can form the target, we have successfully found the pair

            
            Test case 2: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5, 4, 6]
                - Discard any triplet whose a > 5 or b > 4 or c > 6
                - Discard [2, 5, 6] and [5, 7, 5]
                - Left with [1, 4, 4] != [5, 4, 6] since it is the only one, so we return False

            Test case 3: triplets=[[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target=[5,5,5]
                - Discard any triplet whose a > 5, b > 5 or c > 5
                - All of them are still valid
                - res = [5, 5, 5]
            One edge case is if len(triplets) == 1, and it is not equal to target already, then we return false. 

        QUESTION: 
        - Can we perform the operations on each triplet when it is modified? Or must it be strictly using the values that are present inside triplets. Say i modified the first 2 triplets and took the max of each element, can I use this result and perform it on other triplets as well?
        """

        # 1. Cleaning the triplets array to remove any triplet whose a > target_a or b > target_b or c > target_c
        valid_triplets = [] # To store only the valid triplets
        for triplet in triplets:
            a, b, c = triplet[0], triplet[1], triplet[2]
            if a <= target[0] and b <= target[1] and c <= target[2]:
                # Then this is a valid candidate
                valid_triplets.append(triplet)
        
        print("List of valid triplets are", valid_triplets)


        # 2. Edge case handling: 
        # If no valid triplets return False
        if not valid_triplets:
            return False
        
        # If only 1 triplet, check wheter it is equal to target or not
        if len(valid_triplets) == 1:
            return valid_triplets[0] == target
        
        # Otherwise, there are at least 2 triplets, which we can perform operations on continuosly
        res = [-1, -1, -1] # To store the resultant maximum of everything
        for i in range(len(valid_triplets)):
            first = valid_triplets[i]
            res[0] = max(first[0], res[0])
            res[1] = max(first[1], res[1])
            res[2] = max(first[2], res[2])
        return res == target 

        
        


