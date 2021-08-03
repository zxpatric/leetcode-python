
def __searchIn(alist, first, last, value):
    if first == last:
        if alist[first] == value:
            return first
        else:
            return -1
    else:
        pivot = int((first + last) / 2.0)
        if alist[pivot] == value:
            return pivot
        elif alist[pivot] > value:
            return __searchIn(alist, first, pivot, value)
        else:
            return __searchIn(alist, pivot+1, last, value)

def searchSorted (alist, value):
    print(alist)
    num = len(alist)
    if (num < 1):
        return -1
    index=__searchIn(alist, 0, num-1, value)

    result = []
    if index < 0:
        return result
    else:
        left_index = index-1;
        while left_index>=0 and alist[left_index]==value:
            result.insert(0, left_index)
            left_index = left_index - 1

        result.append(index);
        right_index = index +1;
        while right_index<num and alist[right_index]==value:
            result.append(right_index)
            right_index = right_index + 1

    return result