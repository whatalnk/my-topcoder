# SRM 671 Div2 Easy
# [Very short Editorial of SRM #671 - Codeforces](http://codeforces.com/blog/entry/20939)
class BearPaints():
    def maxArea(self, w, h, m):
        area = 1
        for i in range(1,w+1):
            area = max(area, i * min(m/i, h))
        return area