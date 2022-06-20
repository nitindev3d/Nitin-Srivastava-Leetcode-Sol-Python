class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 10001
        m = 0
        for i in range(len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
            if prices[i]- minimum > m:
                m = prices[i] - minimum
        return m