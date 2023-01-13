from collections import Counter

c = Counter('aabbcc')
try:
    odd = next(v for v in c.values() if v % 2 == 1)
except StopIteration:
    odd = False
print(odd)