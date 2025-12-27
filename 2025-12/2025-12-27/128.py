class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set = set(nums)
        count = 0

        for num in new_set:
            if (num - 1) not in new_set:
                length = 1
                while (num + length) in new_set:
                    length += 1
                count = max(length, count)
        return count
