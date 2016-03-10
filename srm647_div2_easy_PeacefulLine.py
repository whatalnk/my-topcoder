# SRM 647 Div2 Easy
# http://community.topcoder.com/stat?c=problem_statement&pm=13632

class PeacefulLine():
    def makeLine(self, x):
        d = {}
        for i in x:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        if len(x) % 2 == 0:
            lim = len(x)//2 + 1
        else:
            lim = len(x)//2 + 2
        if max(d.values()) < lim:
            return "possible"
        else:
            return "impossible"