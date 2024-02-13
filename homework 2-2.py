import numpy as np

class SumTree:

    def __init__(self, data: list):
        ln = len(data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = data
        else:
            self.data = data
            lb = int(lb) + 1
            for i in range(ln, 2 ** lb):
                self.data.append(0)

        self.tree = [0 for i in range(len(self.data) - 1)] + self.data
        self.calc_tree()




    def calc_tree(self) -> None:
        for i in range(len(self.tree) + 1, 2, -2):
            s1 = self.tree[i - 2]
            s2 = self.tree[i - 3]
            sm = s1 + s2
            self.tree[(i - 4) // 2] = sm




def Sum(tree, l: int, r: int):

    def tree_sum(l: int, r: int, tl=0, tr=len(tree.data) - 1):  # len(tree.data)-1

        root = tree.tree[0]
        # left from root - [0,(len(self.data))//2]
        # right from root - [len(self.data)//2,len(self.data)]
        sum = 0

        # если встретили лист
        tm = (tl + tr + 1) // 2
        if tr == tl:
            return tree.data[tm]

        # если отрезок на который смотрим полностью внутри запрашиваемого
        if l < tl and r >= tr:

            index1 = (len(tree.data) - 1) + tr  # 14
            index2 = (len(tree.data) - 1) + tl+1  # 8

            while index1 != index2:
                index1 = max((index1 - 2) // 2, 0)  # 6
                index2 = max((index2 - 2) // 2, 0)  # 3
            if tl + 1 == tr:
                return tree.tree[(index1 - 2) // 2]
            else:
                return tree.tree[index1]

        # если надо, спускаемся по дереву дальше
        go_left = l < tm
        go_right = r >= tm

        print(go_left, go_right, tl, tr, tm)

        if go_left:
            sum += tree_sum(l, r, tl=tl, tr=tm - 1)
        if go_right:
            sum += tree_sum(l, r, tl=tm, tr=tr)

        return sum

    return tree_sum(l, r)

def addingwithoutdumatb(tree : list, place, added):

    newtree = (tree[len(tree)//2:])
    while len(newtree)<(place):
        newtree.append(0)
    newtree[place-1]=newtree[place-1]+added
    tree = SumTree(newtree)
    return tree

tree = SumTree([1,2,3,4,5,6,7,8])
#print(tree.tree)

#tree = addingwithoutdumatb( tree.tree, 1,5)

print(tree.tree)

print(Sum(tree,2,5))



