# method 1
# from right to left
class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0
        for i in s[::-1]:
            curr = trans[i]
            if curr >= prev:
                result += curr
            else:
                result -= curr
            prev = curr
        return result


# method 2
# from left to right
class Solution2:
    def romanToInt(self, s: str) -> int:
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 100000
        for i in s:
            curr = trans[i]
            if curr <= prev:
                result += curr
            else:
                result = result + curr - 2 * prev
            prev = curr
        return result


s = Solution()
print(s.romanToInt("III"))  # 3
print(s.romanToInt("IV"))  # 4
print(s.romanToInt("IX"))  # 9
print(s.romanToInt("LVIII"))  # 58
print(s.romanToInt("MCMXCIV"))  # 1994
