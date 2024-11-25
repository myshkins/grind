def solution(s: str, t:str):
    result = 0
    slist = [c for c in s]
    tlist = [c for c in t]
    for c, v in enumerate(slist):
        if v.isdigit():
            temp = slist[:c] + slist[c + 1:]
            temp_str = "".join(temp)
            if temp_str < t:
                result += 1
    for c, v in enumerate(tlist):
        if v.isdigit():
            temp = tlist[:c] + tlist[c + 1:]
            temp_str = "".join(temp)
            if temp_str > s:
                result += 1
    return result
