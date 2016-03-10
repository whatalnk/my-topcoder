import math
class PalindromePrime:
    def isPrime(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            lim = int(math.sqrt(n)) + 1
            for i in range(2, lim):
                if n % i == 0:
                    return False
            return True

    def count(self, L, R):
        res = 0
        for n in range(L, R+1):
            if self.isPrime(n):
                nstr = str(n)
                if nstr == nstr[::-1]:
                    res += 1
        return res