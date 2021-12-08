import math

class Solution:
    def maxProfit(self, k, prices):                
        N = len(prices)
        if k < 1 or N < 2: return 0
        K = 2 * k
        states = [-math.inf] * (K)        
        states[0] = -prices[0]            
        for i in range(1, N):
            states[0] = max(states[0], -prices[i])
            for j in range(1, K):
                if j % 2 == 1:
                    states[j] = max(states[j], states[j-1] + prices[i])
                else:
                    states[j] = max(states[j], states[j-1] - prices[i])        
        return max(0 , states[-1])
        