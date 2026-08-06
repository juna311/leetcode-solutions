class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        firstString = {}
6        for i in range(0, len(s)):
7            if s[i] in firstString:
8                firstString[s[i]] = firstString[s[i]] + 1
9            else:
10                firstString[s[i]] = 1
11        for j in range(0, len(t)):
12            if t[j] in firstString:
13                firstString[t[j]] = firstString[t[j]] - 1
14            else:
15                firstString[t[j]] = -1
16        for k in firstString.values():
17            if k != 0:
18                return False
19        return True