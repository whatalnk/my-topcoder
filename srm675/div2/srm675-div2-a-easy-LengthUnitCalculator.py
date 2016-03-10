# [TopCoder Statistics - Problem Statement](https://community.topcoder.com/stat?c=problem_statement&pm=14090&rd=16625)
# [null](https://community.topcoder.com/stat?c=problem_solution&cr=22676962&rd=16625&pm=14090)
class LengthUnitCalculator():
    def calc(self, amount, fromUnit, toUnit):
        amount = float(amount)
        units = {"mi": 1, "yd": 1760, "ft": 1760 * 3, "in": 1760 * 3 * 12}
        return amount * units[toUnit] / units[fromUnit]