def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        n=len(prices)
        low=prices[0]
        dp=[0]*n
        mprofit=0
        for i in range(1,n):
            dp[i]=dp[i-1]
            if prices[i]-low > mprofit:
                mprofit=prices[i]-low
                dp[i]=mprofit
            elif prices[i] < low:
                low=prices[i]
        #print dp
        rdp=[0]*(n+1)
        mmax=prices[n-1]
        mprofit=0
        for i in range(n-2,1,-1):
            rdp[i]=rdp[i+1]
            if mmax-prices[i] > mprofit:
                mprofit=mmax-prices[i]
                rdp[i]=mprofit
            elif prices[i] > mmax:
                mmax=prices[i]

        #print rdp
        maxprofit=0
        for i in range(n):
            maxprofit=max(dp[i]+rdp[i+1], maxprofit)

        return maxprofit