from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        result = []
        # Create a counter object which counts number of times numbers appear in nums list
        counter = Counter(nums)
        # Use collections built in most_common to sort values from most common to least
        most_common = counter.most_common(k)
        
        for num, freq in most_common:
            result.append(num)

        return result