# SRM 646 Div2 Easy
class TheConsecutiveIntegersDivTwo():
    def find(self, numbers, k):
        if k == 1:
            return 0
        else:
            n_sorted = sorted(numbers)
            n_diff = [n_sorted[i+1] - n_sorted[i] for i in range(len(numbers)-1)]
            return min(n_diff) - 1