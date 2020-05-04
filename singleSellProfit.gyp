def DynamicProgrammingSingleSellProfit(arr):
    # If the array is empty, we cannot make a profit.
    if len(arr) == 0:
        return 0

    # Otherwise, keep track of the best possible profit and the lowest value
    # seen so far.
    profit = 0
    cheapest = arr[0]

    # Iterate across the array, updating our answer as we go according to the
    # above pseudocode.
    for i in range(1, len(arr)):
        # Update the minimum value to be the lower of the existing minimum and
        # the new minimum.
        cheapest = min(cheapest, arr[i])

        # Update the maximum profit to be the larger of the old profit and the
        # profit made by buying at the lowest value and selling at the current
        # price.
        profit = max(profit, arr[i] - cheapest)

    return profit