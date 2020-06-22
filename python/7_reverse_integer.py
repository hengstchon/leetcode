# method 1
# int -> str -> int
class Solution:
def reverse(self, x: int) -> int:
    sign = 1
    if x < 0:
        x = -x
        sign = -1

    result = int(str(x)[::-1])

    max = pow(2, 31) - 1
    min = -pow(2, 31)
    if result > max or result < min:
        return 0
    return sign * result


# method 2
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        result = 0
        while x:
            result = result * 10 + x % 10
            x = x // 10

        max = pow(2, 31) - 1
        min = -pow(2, 31)
        if result > max or result < min:
            return 0
        return sign * result


s = Solution()
print(s.reverse(123))  # 321
print(s.reverse(-123))  # -321
print(s.reverse(120))  # 21
print(s.reverse(1534236469))  # 0
