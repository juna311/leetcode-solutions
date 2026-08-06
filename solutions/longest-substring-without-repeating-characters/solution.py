class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = set()
        maxLength = 0

        for right in range(len(s)):
            while s[right] in answer:
                answer.remove(s[left])
                left += 1
            answer.add(s[right])
            currentLength = len(answer)
            maxLength = max(maxLength, currentLength)
        
        return maxLength

        