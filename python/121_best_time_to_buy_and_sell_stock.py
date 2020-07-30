import unittest
from typing import List


"""
思路：
当 p 循环时， min_price 为 p 之前的最小值
将移动的 p 选定为最大值
在每一次循环中， p-min_price 为在 p 点卖时的最大收益
再取所有 p-min_price 里的最大值
"""
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(max_profit, p - min_price)
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        m = n = 0
        for i in range(1, len(prices)):
            m = max(0, m + prices[i] - prices[i - 1])
            n = max(n, m)
        return n


class Test(unittest.TestCase):
    def test(self):
        s = Solution2()
        data = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
        for d in data:
            print(d)
            self.assertEqual(s.maxProfit(d[0]), d[1])


if __name__ == "__main__":
    unittest.main()
