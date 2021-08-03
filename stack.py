import sys

def runStackTest(aList):
    result = []
    while len(aList)>0:
        result.append(aList.pop())
    return result;


class MinStack ():

    @property
    def mins(self):
        return self.__mins

    def __init__(self):
        self.__data = []
        self.__mins = []

    def push(self, i):
        self.__data.append(i)
        if len(self.__mins)==0 or i<=self.__mins[-1]:
            self.__mins.append(i)

    def pop(self):
        popout = self.__data[-1]
        if popout == self.__mins[-1]:
            self.__mins.pop()
        self.__data.pop()

    def top(self):
        return self.__data[-1]

    def getMin(self):
        return self.__mins[-1]

def test_MinStack():
    ms = MinStack()
    # ms.push(3)
    # ms.push(9)
    # ms.push(2)
    # ms.push(4)
    # ms.push(1)

    ms.push(0)
    ms.push(1)
    ms.push(0)

    print ('min', ms.getMin(), ms.mins)

    ms.pop()
    print('min', ms.getMin(), ms.mins)

    ms.pop()
    # ms.pop()
    print('min', ms.getMin(), ms.mins)
