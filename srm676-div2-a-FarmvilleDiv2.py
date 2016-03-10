from collections import deque
class FarmvilleDiv2:
    def minTime(self, time, cost, budget):
        n = len(time)
        time_sum = sum(time)
        time_cost = deque(sorted([(a, b) for (a, b) in zip(time, cost)], key=lambda tup: tup[1]))
        for i in range(n):
            t, c = time_cost.popleft()
            a = min(t, budget/c)
            time_sum -= a
            budget -= a * c
        return(time_sum)