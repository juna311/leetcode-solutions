class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        longest = 0
        
        for number in numberSet:
            if number - 1 not in numberSet:
                currentNumber = number
                currentLength = 1

                while currentNumber + 1 in numberSet:
                    currentNumber += 1
                    currentLength += 1
                if longest < currentLength:
                    longest = currentLength
        return longest
                

