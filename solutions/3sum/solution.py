class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = list([])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                return answer

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    right -=1
                    left += 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return answer 
        
                