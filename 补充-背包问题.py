'''
简单01背包
'''

def Bag(n, weights, values, cap):
    dplist = [0 for j in range(cap+1)]
    for i in range(cap+1):
        if weights[0] <= i:
            dplist[i] = values[0]
    for i in range(1, n):
        for j in range(cap, -1, -1):
            if weights[i] <= j:
                dplist[j] = max(dplist[j], values[i] + dplist[j-weights[i]])
    return dplist[cap]

'''
存在负重量、负价值的背包问题
'''

def Bag2(n, weights, values, cap):
    ans = 0
    # 先将所有负容量的背包转换为正容量的
    for i in range(n):
        if weights[i] < 0:
            ans += values[i]
            cap -= weights[i]
            weights[i] = -weights[i]
            values[i] = -values[i]
    dplist = [0 for j in range(cap+1)]
    for i in range(cap+1):
        if weights[0] <= i:
            dplist[i] = values[0]
    for i in range(1, n):
        for j in range(cap, -1, -1):
            if weights[i] <= j:
                dplist[j] = max(dplist[j], values[i] + dplist[j-weights[i]])
    return dplist[cap] + ans