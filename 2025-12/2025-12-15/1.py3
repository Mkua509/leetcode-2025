class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {} # Value : Index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevHash:
                # Return indices of the previous complement and the current element
                return [prevHash[diff], index]
            # Store the current number as key and its index as value
            prevHash[num] = index
        return
    
