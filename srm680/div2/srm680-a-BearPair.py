import itertools
class BearPair:
    def bigDistance(self, s): 
        n = len(s)
        res = -1
        for e in itertools.combinations(xrange(n), 2):
            i = e[0]
            j = e[1]
            if s[i] != s[j]:
                res = max(res, abs(i - j))
        return res
