class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = left

            for j in range(left, right):
                if nums[j] <= nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            nums[i], nums[right] = nums[right], nums[i]
            
            if i == target:
                return nums[i]
            elif i < target:
                left = i + 1
            else:
                right = i - 1
