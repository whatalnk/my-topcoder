# SRM #645 Div2 Easy
class BacteriesColony():
    def performTheExperiment(self, c):
        while True:
            diff = [0] * len(c)
            for i in range(1, len(c)-1):
                if c[i] > c[i-1] and c[i] > c[i+1]:
                    diff[i] = -1
                elif c[i] < c[i-1] and c[i] < c[i+1]:
                    diff[i] = 1
            if all([i == 0 for i in diff]):
                break
            c = [i + j for i, j in zip(c, diff)]
        return c
