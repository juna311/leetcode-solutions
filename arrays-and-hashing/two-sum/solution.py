class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {};
        for i in range(0, len(nums)):
            neededNum = target - nums[i]
            if neededNum in needed:
                solution = [i, needed[neededNum]]
                return solution;
            else:
                needed[nums[i]] = i