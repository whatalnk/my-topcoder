class ThePhantomMenace:
    def find(self, doors, droids): 
        if type(doors) == int:
            doors = [doors]
        else:
            doors = list(doors)
        if type(droids) == int:
            droids = [droids]
        else:
            droids = list(droids)
        res = 0
        for d in doors:
            safety = min([abs(d - i) for i in droids])
            res = max([res, safety])
        return res