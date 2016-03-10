class LuckyXor():
  def construct(self, a):
    for i in range(a+1, 101):
      tmp = a ^ i
      if tmp in [4, 44, 7, 77]:
        return i
        break
    if i == 100:
      return -1
