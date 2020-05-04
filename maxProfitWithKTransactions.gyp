def maxProfitWithKTransactions(prices, k):
    i = 0
    b = i
    s = i + 1
    resultA = 0
    resultB = 0
    t = 0
    
    if( len(prices) > 2 and k > 0 ):
        while( k > 1 ):
            if( prices[s] > prices[b] ):
                if( prices[s+1] >= prices[s] ):
                    s += 1 
                else:
                    k -= 1
                    resultA += ( prices[s] - prices[b] )
                    b = s + 1 
                    s = b + 1
                    
            else:
                b = s
                s += 1
            
        if( k == 1 ):
            profit = 0
            menorValor = prices[0]
                
            for i in range(1, len(prices)):
                menorValor = min(menorValor, prices[i])
                profit = max(profit, prices[i] - menorValor)
                #return profit
            resultB = profit
        
        return (resultA + resultB)

    # if the array has only two items and i+1 is grater than i
    if( len(prices) > 1 and prices[s] > prices[b] and k > 0):
        return prices[s] - prices[b]
    
    return 0