class BearCheats:
  def eyesight(self, a, b):
    res = 0
    for(i, j) in zip(list(str(a)), list(str(b))):
      if i != j:
        res += 1
    if res <= 1:
      return "happy"
    else:
      return "glasses"
