class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set(nums)
        if len(unique_elements) < len(nums):
            return True
        else:
            return False