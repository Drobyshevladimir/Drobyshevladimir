class Heap:
    def init(self):
        self.root = None
class Node:
    def init(self,value, left =None, right = None):
        self.left = left
        self.__right = right
        self.__value = value
    def set_value(self):
        return self.__value
    def set_child(self,node, side='left'):
        if side == 'left':
            return
        elif side == 'right':
            return
        else:
            return ValueError  
    def __str(self):
        return str(self.value)

    def __repr(self):
        nodes_list = []
        if self.__left:
            nodes_list.append(self.__left)
        if self.__right:
            nodes_list.append(self.__right)
        while self.__left:
            nodes_list.append()
        return str(self.__value)
    
    def get_value(self):
        return self.__value

    def get_child(self, side = 'left'):
        if side=='left':
            return self.__left
        elif side == 'right':
            return self.__right
        else:
            return ValueError

first_node = Node(5)
second_node = Node(4)
third_node = Node(3, left=first_node, right=second_node)
cinco_node = Node(2)
quatro_node = Node(1, left=third_node, right=cinco_node )
print(quatro_node)
