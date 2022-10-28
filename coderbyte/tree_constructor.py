
class Tree:
    def __init__(self, conns: list, length: int):
        self.conns = conns
        self.parents = [None for _ in range(length + 1)]
        self.kids = [[] for _ in range(length + 1)]
        self.root = None
    
    def build_tree(self):
        for n in self.conns:
            if self.parents[n[0]] is not None:
                return 'false'
            self.parents[n[0]] = n[1]
            if len(self.kids[n[1]]) >= 2:
                return 'false'
            self.kids[n[1]].append(n[0])
        return [self.parents, self.kids]

    def get_root(self):
        x = next(i for i in self.parents if i is not None)
        while x is not None:
            self.root = x
            x = self.parents[x]
        return self.root

    def check_tree(self):
        count = [0]
        def inner_check(parent):
            count[0] += 1
            for k in self.kids[parent]:
                inner_check(k)
        inner_check(self.root)
        if (count[0] - 1) != len(self.conns):
            return 'false'
        else:
            return 'true'




def TreeConstructor(strArr):
    '''Have the function TreeConstructor(strArr) take the array of strings 
    stored in strArr, which will contain pairs of integers in the following
    format: (i1,i2), where i1 represents a child node in a tree and the second
    integer i2 signifies that it is the parent of i1. Your program should, in
    this case, return the string true because a valid binary tree can be formed.
    If a proper binary tree cannot be formed with the integer pairs, then return
    the string false. All of the integers within the tree will be unique, which 
    means there can only be one node in the tree with the given integer value.'''
    conns = [list(map(int, (x.removeprefix('(').removesuffix(')').split(',')))) for x in strArr]
    max0 = max(max(conns, key=lambda x: x[0]))
    max1 = max(max(conns, key=lambda x: x[1]))
    length = max(max0, max1)
    tree = Tree(conns, length)
    if not tree.build_tree():
        return 'false'
    tree.get_root()
    print(tree.check_tree())


test1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)", "(6,7)", "(3,6)", "(8,6)"]
#Output: true
test2 = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
#Output: false 

TreeConstructor(test1)