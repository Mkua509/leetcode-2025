class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set(nums)
        if len(seen) < len(nums):
            return True
        return False