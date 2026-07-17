class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        firstString = {}
        for i in range(0, len(s)):
            if s[i] in firstString:
                firstString[s[i]] = firstString[s[i]] + 1
            else:
                firstString[s[i]] = 1
        for j in range(0, len(t)):
            if t[j] in firstString:
                firstString[t[j]] = firstString[t[j]] - 1
                if firstString[t[j]] == -1:
                    return False
            else:
                return False
        for k in firstString.values():
            if k != 0:
                return False
        return True

