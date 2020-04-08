# bisect.bisect_left(nums, target)

# method 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l != h:
            mid = (l + h) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid
        if target > nums[l]:
            return l + 1
        return l


# method 2
# set h to len(nums)
# so there is a place for target > nums[-1]
# do not need to evaluate if target > nums[h] in last solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        while l != h:
            mid = (l + h) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid
        return l
