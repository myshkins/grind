from copy import copy
def MinWindowSubstring(strArr):
    lst = list(strArr[0])
    query = list(strArr[1])
    
    i = 0   #start from begginning and increment until full query found
    j = 0
    left_buff = copy(query)
    while len(left_buff) > 0:   
        if lst[i] in left_buff:
            left_buff.remove(lst[i])
        i += 1
    left_buff = copy(lst[j:i])
    while left_buff[j] not in query or left_buff.count(left_buff[j]) > query.count(left_buff[j]):
        left_buff.remove(left_buff[j])
    if len(left_buff) == len(query):
        return "".join(left_buff)

    k = len(lst) -1 #start from end and decrement until full query found
    right_buff = copy(query)
    while len(right_buff) > 0:
        if lst[k] in right_buff:
            right_buff.remove(lst[k])
        k -= 1
    right_buff = copy(lst[k + 1: len(lst)])
    k = 0
    while right_buff[k] not in query or right_buff.count(right_buff[k]) > query.count(right_buff[k]):
        right_buff.remove(right_buff[k])
    if len(right_buff) == len(query):
        return "".join(right_buff)
    if len(right_buff) < len(left_buff):
        return "".join(right_buff)
    else:
        return "".join(left_buff)
    




test1 = ["cccaabbbbrr", "rbac"]
#Output: "caabbbbr"

print(MinWindowSubstring(test1))