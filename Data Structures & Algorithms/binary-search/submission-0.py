class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            medium = (left + right) // 2
            if target == nums[medium]:
                return medium
            elif target > nums[medium]:
                left = medium + 1
            elif target < nums[medium]:
                right = medium - 1
        return -1
                
            
