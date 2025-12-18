class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result


    def decode(self, s: str) -> List[str]:
        result, index = [], 0

        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            result.append(s[j + 1 : j + 1 + length])
            index = j + 1 + length
        return result
