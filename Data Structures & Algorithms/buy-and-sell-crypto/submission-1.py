class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0          
        min_price = prices[0] # =10
        for i in range(1,len(prices)):
            profit=prices[i]-min_price #1-10=-9
            if profit > max_profit:  # -9>0      
                max_profit = profit  
            if prices[i] < min_price:  # 1<10    
                min_price = prices[i] #min porice=10
        return max_profit