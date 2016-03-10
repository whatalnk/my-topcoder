import bisect
class BearChairs:
    def findPositions(self, atLeast, d): 
        res = []
        occupied = []
        for i in atLeast:
            tmp = i
            for j in occupied:
                if j - d < tmp < j + d:
                    tmp = j + d
            res.append(tmp)
            bisect.insort_left(occupied, tmp)
        return tuple(res)
