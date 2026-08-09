class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        maxLength = 0
        char = {}
        left = 0

        for right in range(len(s)):
            if s[right] in char:
                char[s[right]] += 1
            else:
                char[s[right]] = 1
            maxFreq = max(maxFreq, char[s[right]])

            while right - left + 1 - maxFreq > k:
                char[s[left]] -= 1
                left += 1
            currentLength = right - left + 1
            maxLength = max(maxLength, currentLength)
        return maxLength
        
            
    
            