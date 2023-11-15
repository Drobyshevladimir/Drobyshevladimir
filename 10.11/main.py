class Heap:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, value, left=None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value

    def __str__(self):
        return str(self.__value)

    def listing(self):
        nodes_list = []

        if self.__left:
            nodes_list.append(self.__left)
        if self.__right:
            nodes_list.append(self.__right)
        for node in nodes_list:
            if not node:
                continue
            if node.__left:
                nodes_list.append(node.__left)
            else:
                nodes_list.append(None)
            if node.__right:
                nodes_list.append(node.__right)
            else:
                nodes_list.append(None)
        value_list = [self.__value]
        for node in nodes_list:
            if node:
                value_list.append(node.__value)
            else:
                value_list.append(None)

        return value_list

        while self.__left:
            print(self.__left)
        while self.__right:
            print(self.__right)
        if not self.__left and not self.__right:
            return str(self.__value)

    def get_value(self):
        return self.__value

    def get_child(self, side='left'):
        if side == 'left':
            return self.__left
        elif side == 'right':
            return self.__right
        else:
            return ValueError

    def set_child(self, node, side='left'):
        if side == 'left':
            self.__left = node
            return
        elif side == 'right':
            self.__right = node
            return
        else:
            return ValueError

first_node = Node(5)
second_node = Node(4)
third_node = Node(3, left = first_node, right = second_node)
cinco_node = Node(2)
quattro_node = Node(1, left = third_node, right = cinco_node)
print(quattro_node.listing())
print(third_node.listing())
