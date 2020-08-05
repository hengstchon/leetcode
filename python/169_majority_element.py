from typing import List
from collections import Counter


# Brute Force
# Time complexity: O(n*n)
# Space complexity: O(1)
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) // 2
        for n in nums:
            c = sum(1 for e in nums if e == n)
            if c > l:
                return n


# HashMap
# Time complexity: O(n)
# Space complexity: O(n)
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(c.keys(), key=c.get)
        return m


# sorting
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


# dict
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

            if d[i] > len(nums) // 2:
                return i


import unittest


class Test(unittest.TestCase):
    def test(self):
        s = Solution4()
        data = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
        for d in data:
            self.assertEqual(s.majorityElement(d[0]), d[1])


if __name__ == "__main__":
    unittest.main()
