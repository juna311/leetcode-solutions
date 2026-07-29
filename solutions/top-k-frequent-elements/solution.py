class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dictFreq = {}
        freq = [[] for _ in range(n + 1)]
        for i in range(n):
            if nums[i] in dictFreq:
                dictFreq[nums[i]] +=1
            else:
                dictFreq[nums[i]] = 1
        for number, count in dictFreq.items():
            freq[count].append(number)
        result = []
        for i in range(len(freq) - 1, -1, -1):
            chunk = freq[i]
            for j in range(len(chunk)):
                if len(result) == k:
                    return result
                result.append(chunk[j])
        return result