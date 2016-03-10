# SRM 671 Div2 Easy
import collections
import bisect
class BearDartsDiv2():
    def count(self, w):
        dic = collections.defaultdict(list)
        size = len(w)
        for a in range(size):
            for b in range(a + 1, size):
                dic[w[a] * w[b]].append(b)
        for k in dic:
            dic[k] = sorted(dic[k])
        ans = 0
        for c in range(2, size):
            for d in range(c + 1, size):
                if w[d] % w[c]:
                    continue
                if dic[w[d] // w[c]]:
                    ans += bisect.bisect_left(dic[w[d] // w[c]], c)
        return ans
