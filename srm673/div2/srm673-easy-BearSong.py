from collections import defaultdict
class BearSong():
    def countRareNotes(self, notes):
        d = defaultdict(int)
        for i in notes:
            d[i] += 1
        return(len([i for i in d.values() if i == 1]))