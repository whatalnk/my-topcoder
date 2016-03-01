class EqualSubstrings2:
    def get(self, s):
        out = 0
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                for k in range(j,len(s)):
                    l = k + j - i
                    if s[i:j] == s[k:l]:
                        out += 1
