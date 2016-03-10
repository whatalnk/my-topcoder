class Drbalance():
    def lesscng(self, s, k):
        l = list(s)
        res = 0
        while True:
            costs = [l.count("+") - l.count("-")]
            for i in range(len(l)):
                ll = l[:-i]
                costs.append(ll.count("+") - ll.count("-"))
            costs_sum = len([i for i in costs if i < 0])
            if costs_sum > k:
                i = l.index("-")
                l[i] = "+"
                res += 1
            else:
                return res
