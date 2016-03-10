# SRM 672 Div2 Hard
# http://kmjp.hatenablog.jp/entry/2015/10/21/0930
class Tdetectived2():
    def reveal(self, s):
        iss = [0] * (1<<18)
        n = len(s)
        val = [0] * 20
        for i in range(n):
            val[i] = 100
        iss[1] = 1
        for mask in range(1<<n):
            if iss[mask]:
                ma = [0] * 20
                for i in range(n):
                    if mask & (1<<i):
                        for j in range(n):
                            ma[j] = max(int(ma[j]), int(s[i][j]))
                md = -1
                ma2 = 0
                for i in range(n):
                    if (mask & (1<<i)) == 0:
                        if md < ma[i]:
                            md = ma[i]
                            ma2 = 0
                        if md == ma[i]:
                            ma2 |= 1<<i
                for i in range(n):
                    if ma2 & (1<<i):
                        iss[mask | (1<<i)] = 1
                        val[i] = min(val[i], bin(mask).count('1'))
        ret = 0
        for i in range(n):
            ret += i * val[i]
        return ret