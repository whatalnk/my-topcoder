# SRM 672 Div2 Medium
import string
class SubstitutionCipher():
    def decode(self, a, b, y):
        substitution_table = {}
        for k in list(string.ascii_uppercase):
            substitution_table[k] = ""
        listb = list(b)
        lista = list(a)
        for k, v in zip(listb, lista):
            substitution_table[k] = v
        if len([i for i in substitution_table.values() if i == ""]) == 1:
            missingkey = [k for k in substitution_table if substitution_table[k] == ""][0]
            missingvalue = list(set(list(string.ascii_uppercase)).difference(set(substitution_table.values())))[0]
            substitution_table[missingkey] = missingvalue
        listy = list(y)
        y_decoded = []
        for k in listy:
            if substitution_table[k] == "":
                return ""
            else:
                y_decoded.append(substitution_table[k])
        return "".join(y_decoded)