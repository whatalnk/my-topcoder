class Cdgame():
  def rescount(self, a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    res = []
    for i in a:
        for j in b:
            res.append((sum_a-i+j)*(sum_b-j+i))
    return(len(set(res)))