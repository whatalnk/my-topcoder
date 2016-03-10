# SRM 648 Div2 Easy
#http://community.topcoder.com/stat?c=problem_statement&pm=13650
class KitayutaMart2():
    def numBought(self, k, t):
        n = 1
        ksum = k
        while True:
            if ksum == t:
                return n
            n += 1
            ksum += 2**(n-1)*k