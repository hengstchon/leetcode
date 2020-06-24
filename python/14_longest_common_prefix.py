from typing import List

# using zip and set
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        str_zip = zip(*strs)
        for i in str_zip:
            if len(set(i)) > 1:
                break
            result += i[0]
        return result


# Vertical scanning
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        first_str = strs[0]
        for i in range(len(first_str)):
            char = first_str[i]
            for j in range(1, len(strs)):
                s = strs[j]
                if i == len(s) or strs[j][i] != char:
                    return first_str[:i]
        # not break, only one element in strs, or all elements in strs are same
        return first_str


s = Solution2()
print(s.longestCommonPrefix(["flower", "fl", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix([""]))
