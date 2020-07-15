"""
Explanation:
    This is a Fibonacci problem.
    if f(n) is the number of ways for n steps,
    then there are only two ways to climb to nth step:
    1. at (n-2)th step, climb 2 steps
    2. at (n-1)th step, climb 1 step
    So f(n) = f(n-2) + f(n-1)
"""


# O(n) space
class Solution1:
    def climbStairs(self, n: int) -> int:
        res = [1, 1]
        for i in range(2, n + 1):
            res_i = res[i - 1] + res[i - 2]
            res.append(res_i)
        return res[n]


# O(1) space
class Solution2:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


import unittest


class Test(unittest.TestCase):
    def test(self):
        s = Solution2()

        inputs = [[1, 1], [2, 2], [3, 3], [4, 5]]

        for i in inputs:
            self.assertEqual(s.climbStairs(i[0]), i[1])


if __name__ == "__main__":
    unittest.main()
