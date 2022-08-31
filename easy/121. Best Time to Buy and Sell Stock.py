class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        '''
        m_profit = 0
        for i in range(len(prices)):
            for x in prices[i+1:]:
                if x - prices[i] > m_profit:
                    m_profit = x - prices[i]
                    
                    
        return m_profit
        '''
        
        profit = 0                      #maxprofit tracker, initialize to 0
        min_ = prices[0]                #initialize min_ value to the first price in prices
        
        for x in prices[1:]:            #traverse all price (x) in prices, after the first one
            if x > min_ and x - min_ > profit:      #if x is greater than the min_ and if the profit b/w x and the min is greater than profit :
                profit = x - min_                   #record new (greater) profit
                
            if x < min_:                            #if x is less than the min, we make it the new min.
                min_ = x
        
        
        
        return profit                               #return the profit (a number > 0 if there is profit; or 0 if there is no profit)
        
   
        
        
        