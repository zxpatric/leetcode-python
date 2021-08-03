

def sumTwo (alist, target):
    result = []
    valueDict = dict()
    num = len(alist)
    for a,i in zip(alist, range(0,num)):
        valueDict[target - a] = i

    for a,i in zip(alist, range(0,num)):
        index = valueDict.get(a, None)
        if index is not None:
            valueDict.pop(a, None)
            valueDict.pop(target-a, None)
            result.append([i, index])

    return result;