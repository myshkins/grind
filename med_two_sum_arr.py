"""
Given an array of integers a, your task is to find how many of its contiguous
subarrays of length m contain a pair of integers with a sum equal to k.
*note this was a CodeSignal assessment problem. I think the solution is off by
one :o 
"""
def solution(a, m, k):
    result = 0
    subarr = {}
    pairs = {}
    # get initial subarray
    for i, v in enumerate(a[:m]):
        if subarr.get(v) is None:
            subarr[v] = [i]
        else:
            subarr[v] += [i]
    # find initial pairs
    for i, v in enumerate(a[:m]):
        x = subarr.get(v)
        y = subarr.get(k - v)
        if k - v == v:
            if x is not None:
                if len(x) > 1:
                    pairs[i] = x
        elif y is not None:
            if pairs.get(i) is None:
                pairs[i] = y
            else:
                pairs[v] += x
    if len(pairs.items()) > 0:
        result += 1
    # slide the window(subarr) through the rest of the array
    for i, v in enumerate(a[m:], m):
        # pop the leftmost element from subarr, and remove any attached pairs
        left = i - m
        subarr[a[left]].remove(left)
        if len(subarr[a[left]]) == 0:
            subarr.pop(a[left])
        if pairs.get(left) is not None:
            popped = pairs.pop(left)
            for p in popped:
                if len(pairs[p]) == 0:
                    pairs.pop(p)
        # append next element to subarray
        x = subarr.get(v)
        if x is None:
            subarr[v] = [i]
        else:
            subarr[v] += [i]
        # check if new pair to add with new element
        x = subarr.get(v)
        y = subarr.get(k - v)
        if k - v == v:
            if x is not None:
                if len(x) > 1:
                    pairs[i] = x
        elif y is not None:
            if pairs.get(i) is None:
                pairs[i] = y
            else:
                pairs[i] += y
            for p in y:
                if pairs.get(p) is None:
                    pairs[p] = [i]
                else:
                    pairs[p] += [i]
        if len(pairs.items()) > 0:
            result += 1
    return result

a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10
# solution(a, m, k) = 5.
print(solution(a, m, k))

# this solution is off by one