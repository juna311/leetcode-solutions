class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        highestProfit = 0
        for i in range(1, len(prices)):
            if lowestPrice > prices[i]:
                lowestPrice = prices[i]
            else:
                currentProfit = prices[i] - lowestPrice
                if currentProfit > highestProfit:
                    highestProfit = currentProfit
        return highestProfit
