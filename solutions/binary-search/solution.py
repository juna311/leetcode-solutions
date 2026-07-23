class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(left, right):
            if left > right: return -1
            
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return recursive((middle + 1), right)
            else:
                return recursive(left, (middle - 1))

        return recursive(0, (len(nums) - 1))

