def max_profit(prices):
    for i in range(len(prices)-1):
        if prices == sorted(prices, reverse=True):
            return 0
        
        if prices[i] < prices[i+1]:
            
            buy = prices[i]
            break
        
        min_val = min(prices)

        for i in range(len(prices)):
            if prices[i] == min_val:
                index = i
        
    lst = []
    for j in range(i, len(prices)):
        lst.append(prices[j])
    max_val = max(lst)

    if min_val != prices[-1] and prices[index+1] > min_val:
        profit = max_val - min_val
    else:
        profit = max_val - buy

    return profit

prices = [1]
print(max_profit(prices))