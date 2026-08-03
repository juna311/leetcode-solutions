class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for i in range(0, len(nums)):
            if nums[i] in checked:
                return True
            else:
                checked.add(nums[i])
        return False