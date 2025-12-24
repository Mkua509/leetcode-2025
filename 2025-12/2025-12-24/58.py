class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # First find the last letter of the word
        end = len(s) - 1


        # While end is a space move end backwards until its no longer a space or is the start of the list
        while s[end] == " ":
            end -= 1
        

        # Then we start iteration of start from end, then move backwards until it reaches the first space 
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        results = end - start
        # Return the length of list
        return results