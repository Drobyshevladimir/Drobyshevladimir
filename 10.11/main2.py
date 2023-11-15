class Heap:
    def __init__(self):
        self.root = None
    def add(self, node):
        if not self.__root:

    def get_root(self):
        return self.__root
    def add(self, node):
        assert isinstance(node,Node)
        if not self.__root:
            self.__root = node
            return
        current_node = self.__root
        up_node = None
        while node.__value > current_node.__value:
            if not current_node.__left = node:
                 current_node.__left = node
                 return
            up_node = current_node
            current_node = current_node.__left
        if up_node:
            up_node._left = node

        
        while node.__value > current_node.__value:
            if not current_node.left:
                current_node.left = node
                return
            elif not current_node.__right:
                current_node.__right = node
                return


        
class Node:
    def __init__(self, value, left=None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value

    def heaprint(self):
        value_list = self.listing()
        depth = 0
        counter = 0
        floor = []
        print(value_list)
        for i in range(len(value_list)):
            counter += 1
            if value_list[i]:
                floor.append(value_list[i])
            else:
                floor.append(None)

            if 2**depth == counter:
                counter %= (2**depth)
                depth += 1
                print(*floor)
                floor = []
                continue

        return ' '

    def listing(self) -> list:
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

quattro_node.heaprint()
