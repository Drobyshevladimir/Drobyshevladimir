import numpy as np

class SumMassiv:

    def __init__(self, data: list):
        self.data = data
        self.sum =self.data
        self.calc_sum()




    def calc_sum(self) -> None:
        for i in range(1,len(self.sum)):

            self.sum[i] += self.sum[i-1]


def sumsection(spisok, l=int, r=int):
    calc_sum=spisok.sum
    if r>0 and l>-1:
        calc_sum.insert(0,0)
        return(calc_sum[r]-calc_sum[l])
    else:
        return('блин ты чево')







tree = SumMassiv([1,2,3,4,5,6,7,8])

print(tree.sum)

print(sumsection(tree,3,5))
error = SumMassiv([2])
print(sumsection(error,0,1))



