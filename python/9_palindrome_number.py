# method 1
# full check
#  class Solution:
#  def isPalindrome(self, x: int) -> bool:
#  if x < 0:
#  return False
#  ori = x
#  rev = 0
#  while x:
#  rev = rev * 10 + x % 10
#  x = x // 10
#  return ori == rev


# method 2
# half check
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # to get False when x = 10, 20, 30...
        # otherwise, e.g. x = 10
        # before return, x = 0, rev = 1, will return True
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        return x == rev or x == (rev // 10)


s = Solution()
print(s.isPalindrome(121))  # true
print(s.isPalindrome(10))  # false
