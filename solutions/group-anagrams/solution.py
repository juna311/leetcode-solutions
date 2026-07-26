class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)):
            count = [0] * 26
            for j in strs[i]:
                index = ord(j) - ord("a")
                count[index] += 1
            key = tuple(count)
            if key in anagram:
                anagram[key].append(strs[i])
            else:
                anagram[key] = [strs[i]]

        return list(anagram.values())
