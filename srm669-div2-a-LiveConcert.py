class LiveConcert():
  def maxHappiness(self, h, s):
    dict = {}
    m = len(h)
    for (key, val) in zip(s, h):
      if dict.has_key(key):
        dict[key].append(val)
      else:
        dict[key] = [val]
    happiness = 0
    for val in dict.itervalues():
      happiness += max(val)
    return happiness