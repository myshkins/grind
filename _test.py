import itertools as it

def add(a, b):
    if len(a) == len(b):
        long, short = a, b
    else:
        long = max(a, b, key=lambda x: len(x))
        short = min(a, b, key=lambda x: len(x))
    diff = len(long) - len(short)
    buffer = "".join(["0" for _ in it.repeat(None, diff)])
    short = (buffer + short)[::-1]
    long = long[::-1]
    carry = 0
    result = []
    for c, v in enumerate(long):
        bsum = carry + int(v) + int(short[c])
        carry = 0
        if bsum == 1:
            result.append('1')
        else:
            result.append('0')
        if bsum >= 2:
            carry = 1
    result.append(str(carry))       
    final = ("".join(result))[::-1]
    print(final)

add('1010', '1011')