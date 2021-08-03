import itertools

def printAllCombinations (alist, num):
    print(list(itertools.combinations(alist, num)))


def printAllPermutations (alist, num):
    print(list(itertools.permutations(alist, num)))


def sumFour (alist, target):
    result = []
    num = len(alist)
    for iter in itertools.combinations(range(0, num), 4):
        if target == alist[iter[0]] + alist[iter[1]] + alist[iter[2]] +alist[iter[3]]:
             result.append (list(iter))

    return result;