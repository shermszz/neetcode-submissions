class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in myMap:
                print(complement, "found")
                index = myMap[complement]
                print(index, idx)
                if index != idx:
                    #Return idx and index, but smaller one first
                    return sorted([index, idx])
            myMap[num] = idx
            print(myMap)
        return []