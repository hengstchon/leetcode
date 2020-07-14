# regular algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                # if loops to the last char of needle, still not break:
                # return i
                if j == len(needle) - 1:
                    return i
        return -1


# waste more space
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


# python hack
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


import unittest


class SolutionTest(unittest.TestCase):
    def test(self):
        s = Solution()

        inputs = [
            [("hello", "ll"), 2],
            [("hello", "li"), -1],
            [("aaaaa", "bba"), -1],
            [("hello", ""), 0],
        ]

        for i in inputs:
            self.assertEqual(s.strStr(*i[0]), i[1])


if __name__ == "__main__":
    unittest.main()
