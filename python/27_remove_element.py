# method 1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p


# method 2
# use list.remove()
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # copy nums
        for v in nums[:]:
            if v == val:
                nums.remove(v)
        return len(nums)
