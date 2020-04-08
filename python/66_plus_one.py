# three situations to consider:
# 1. the least significant digit is not 9
# 2. the least significant digit is 9
# 3. every digit is 9

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in range(l-1, -1, -1):
            print('i', i)
            print(digits)
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
