from typing import List
import heapq

def max_profit_greedy(stock_prices):
    options = []
    current_profit = 0

    for price in stock_prices:
        if len(options) > 0 and price > options[0]:
            current_profit += price - options[0]
            heapq.heappop(options)
        
        heapq.heappush(options, price)

    return current_profit

print(max_profit_greedy([7, 1, 5, 3, 6, 4]))