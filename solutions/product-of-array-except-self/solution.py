class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        answer = []
        for i in range(len(nums)):
            answer.append(left)
            left = left * nums[i]
        for j in range(len(nums)):
            index = len(nums) - 1 - j
            answer[index] = answer[index] * right
            right = right * nums[index]
        return answer
