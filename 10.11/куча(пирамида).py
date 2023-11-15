class Heep:
    def __init__ (self):
        self.root = None


class node:
    def __init__ (self, value, left = None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value

    def __repr__(self):
        node_list = []
        if self.__left:
            nodes_list.append(self.__left)
        if self.__right:
            nodes_list.append(self.__right)
        while self.__left:     
            print(self.__left)
        while self.right:
            print(self.right)
        if not self.left and not self.right:
            print(self.__value)
        
    
    def get_value(self):
        return self.__value
    
    def get_child(self,node, side = 'left'):
        if side == 'left':
            self.__left = node
            return
        elif side == 'right':
            self.__right = node
            return
        else:
            return ValueError

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
            





            
first_node = node(5)
second_node = node(4)
third_node = node(3, left = first_node, right = second_node)
cinco_node = node(2)
quattro_node = node(1, left = third_node, right = cinco_node)
print(quattro_node.listing())
print(third_node.listing())
