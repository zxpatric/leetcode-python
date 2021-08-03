class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # def intersect (self, another:Interval):
    #     return self.start <

    def resolve (self, another):
        if another.start > self.end or another.end < self.start:
            return False, None
        else:
            return True, Interval(min(self.start,another.start), max(self.end,another.end))

    def __str__(self):
        return "(" + str(self.start) + "," + str(self.end) + ")"

    def __repr__(self):
        return self.__str__()

def resolve (one, another):
    if another.start > one.end or another.end < one.start:
        return False, None
    else:
        return True, Interval(min(one.start, another.start), max(one.end, another.end))

def lessthan(one, another):
    return one.end < another.start

class Solution:
    @classmethod
    def insert(cls, intervals, newInterval):
        num = len(intervals)
        index = num
        for i in range (num-1, -1, -1):
            _interval = intervals[i]
            # ret, another = newInterval.resolve(_interval)
            ret, another = resolve(newInterval, _interval)
            if ret:
                intervals.remove(_interval)
                newInterval = another
                index=i
            else:
                if lessthan(newInterval, _interval):
                    index=i


        intervals.insert(index, newInterval)

        return intervals;
