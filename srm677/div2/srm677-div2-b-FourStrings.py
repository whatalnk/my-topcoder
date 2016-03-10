import itertools
class FourStrings:
    def cnct(self, s1, s2):
        if s2 in s1:
            return s1
        else:
            for i in range(1, len(s2)):
                if s1.endswith(s2[:(i * -1):]):
                    return s1 + s2[(len(s2) - i)::]
            return s1 + s2

    def shortestLength(self, a, b, c, d):
        res = len(a + b + c + d)
        for strlist in itertools.permutations([a, b, c, d]):
            ss = strlist[0]
            for i in range(1, 4):
                ss = self.cnct(ss, strlist[i])
            res = min(res, len(ss))
        return res