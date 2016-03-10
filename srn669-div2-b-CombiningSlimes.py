from collections import deque
class CombiningSlimes():
  def maxMascots(self, a):
    mascots = 0
    aa = deque(sorted(a))
    while len(aa) != 1:
      l = aa.popleft()
      r = aa.pop()
      aa.append(l+r)
      mascots += l*r
    return(mascots)