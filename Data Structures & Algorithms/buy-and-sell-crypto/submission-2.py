class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  [10,2,5,6,7,1,5]
        i = 0 
        length = len(prices)
        min_price = float('inf')
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > profit:
                profit = price-min_price
        
        return profit