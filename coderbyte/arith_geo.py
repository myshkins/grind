def ArithGeo(arr):
    '''Have the function ArithGeo(arr) take the array of numbers stored in arr 
    and return the string "Arithmetic" if the sequence follows an arithmetic 
    pattern or return "Geometric" if it follows a geometric pattern. If the 
    sequence doesn't follow either pattern return -1. An arithmetic sequence is
    one where the difference between each of the numbers is consistent, where 
    as in a geometric sequence, each term after the first is multiplied by 
    some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and 
    Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as 
    parameters, 0 will not be entered, and no array will contain all the 
    same elements. '''
    answer = ''
    if (diff := arr[2] - arr[1]) == arr[1] - arr[0]:
        answer = 'arithmetic'
    elif (fact := arr[2] / arr[1]) == arr[1] / arr[0]:
        answer = 'geometric'
    else:
        answer = -1
        return answer
    if answer == 'arithmetic':
        for count, value in enumerate(arr[1:]):
            if value - arr[count] != diff:
                answer = -1
                return answer
        return answer
    elif answer == 'geometric':
        for count, value in enumerate(arr[1:]):
            if value / arr[count] != fact:
                answer = -1
                return answer
        return answer
    return answer


test1 = [5,10,15]
# Output: Arithmetic

test2 = [2,4,16,24]
# Output: -1 