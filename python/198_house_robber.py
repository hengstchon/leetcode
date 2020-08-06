import unittest
from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], nums[i] + res[i - 2])
        print(res)
        return res[-1]


# time: O(n)
# space: O(1)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            a, b = b, max(a + n, b)
        return b


class Test(unittest.TestCase):
    def test(self):
        s = Solution2()
        data = [([1, 2, 3, 1], 4), ([2, 7, 9, 3, 1], 12)]
        for d in data:
            self.assertEqual(s.rob(d[0]), d[1])


if __name__ == "__main__":
    unittest.main()
