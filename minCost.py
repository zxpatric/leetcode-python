def minCostClimbingStairs(cost):
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
    return min(f1, f2)

# f[i] = cost[i] + min(f[i+1], f[i+2])

def test_minCost():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print (minCostClimbingStairs (cost))