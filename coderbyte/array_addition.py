from itertools import combinations

def ArrayAdditionI(arr):
    '''Have the function ArrayAdditionI(arr) take the array of numbers stored in
    arr and return the string true if any combination of numbers in the array
    (excluding the largest number) can be added up to equal the largest number'
    in the array, otherwise return the string false. For example: if arr
    contains [4, 6, 23, 10, 1, 3] the output should return true because
    4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the
    same elements, and may contain negative numbers.'''
    array = arr
    m = max(array)
    array.remove(m)
    for i in range(len(array)):
        combos = list(combinations(array, i+1))
        sums = map(sum, combos)
        if m in sums:
            return True
    return False
        



test1 = [5,7,16,1,2]
#Output: false
test2 = [3,5,-1,8,12]
#Output: true 
print(ArrayAdditionI(test1))