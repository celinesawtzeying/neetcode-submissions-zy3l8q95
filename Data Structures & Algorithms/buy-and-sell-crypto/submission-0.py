# go through the prices
# "Is this the cheapest price I've seen so far?" → update your buy price
# "If I sell today, what's my profit?" → update your max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)
        return max_profit



        
        