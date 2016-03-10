class BearSlowlySorts():
    def minMoves(self, w):
        w = list(w)
        if w == sorted(w):
            return 0
        else:
            minw = min(w)
            maxw = max(w)
            if minw == w[0]:
                return 1
            elif maxw == w[-1]:
                return 1
            elif maxw == w[0]:
                if minw == w[-1]:
                    return 3
                else:
                    return 2
            else:
                return 2