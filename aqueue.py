# import queue
import collections

def runStackTest(aList):
    result = collections.deque()
    for a in aList:
        result.append(a)

    while result:
        print(result.pop())

    # return result;


def runQueueTest(aList):
    result = collections.deque()
    for a in aList:
        result.appendleft(a)
    while result:
        print(result.pop())
    # return result;

def runQueueTest2(aList):
    result = collections.deque()
    for a in aList:
        result.append(a)
    while result:
        print(result.popleft())
    # return result;
