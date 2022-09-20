def hans(area, tulipArea, tulipTime, tulipPrice, roseArea, roseTime, rosePrice, maxTime):
    maxTulip = int(area // tulipArea)
    highestProfit = 0
    solution = ""
    for tulips in range(maxTulip+1):
        areaLeft = area - tulips * tulipArea
        roses = int(areaLeft // roseArea)
        timeSpent = tulips * tulipTime + roses * roseTime
        if timeSpent <= maxTime:
            profit = tulips * tulipPrice + roses * rosePrice
            if profit > highestProfit:
                highestProfit = profit
                solution = str(tulips) + ":" + str(roses)
    return solution

print(hans(20, 0.4, 0.5, 50, 0.6, 1, 75, 30))