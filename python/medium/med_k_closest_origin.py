# class Solution:
#     def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
#         res = []
#         for point in points:
#             d = ((point[0] ** 2) + (point[1] ** 2)) ** .5
#             res.append((d, point[0], point[1]))
#         res.sort(key=lambda x: x[0])
#         result = [(item[1], item[2]) for item in res[:k]]
#         return result


class Solution:
    def comparator(self, a: list, b: list) -> bool:
        a_dist = (((a[0] ** 2) + (a[1] ** 2)) ** .5, a[0], a[1])
        b_dist = (((b[0] ** 2) + (b[1] ** 2)) ** .5, b[0], b[1])
        if a_dist <= b_dist:
            return True
        else:
            return False

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        for point in points:
            # initially fill the res array with first k elements in heap order
            # actually k + 1 elements to have room for swapping
            if len(res) < k + 1:
                res.append(point)
                j = len(res) - 1
                while self.comparator(res[j], res[j // 2]) and j > 0:
                    # exchange elements in array
                    res[j], res[j // 2] = res[j // 2], res[j]
                    j //= 2
            # then begin adding and maintaining heap order 
            else:
                p = k - 1
                if self.comparator(res[p], point):
                    continue
                else:
                    # put element at end in buffer position (k + 1)
                    res[k] = point
                    while self.comparator(point, res[p]) and p > 0:
                        res[p], res[k] = res[k], res[p]
                        p //= 2

        return res[:-1]


input1 = [[3, 3], [5, -1], [-2, 4]]
k1 = 2
# Output: [[3,3],[-2,4]]
input2 = [[0, 1], [0, 1]]
k2 = 2
s = Solution()
print(s.kClosest(input2, k2))