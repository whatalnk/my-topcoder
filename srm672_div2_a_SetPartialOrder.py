# SRM 672 Div2 Easy
class SetPartialOrder():
    def compareSets(self, a, b):
        seta = set(a)
        setb = set(b)
        if seta == setb:
            return "EQUAL"
        elif seta.issubset(setb):
            return "LESS"
        elif setb.issubset(seta):
            return "GREATER"
        else:
            return "INCOMPARABLE"
