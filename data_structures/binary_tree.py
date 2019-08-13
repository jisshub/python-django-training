# Binary Tree Implementation
# using oop

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class Binary:

    def __init__(self):
        self.root = None

    #         here this init method sets root node as None.

    def insert(self, value=24):
        if self.root is None:
            # if root of the tree is none, then call the class init of Node and set root as value.
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    #             here v invoke the private method. _insert

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                # cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)

            else:
                self._insert(value, cur_node.right_child)
        else:
            print('ok')

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):

        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))

            self._print_tree(cur_node.right_child)

    def search_tree(self, value):
        if self.root is not None:
            # self._print_tree(self.root)
            return self._search_tree(value, self.root)
        else:
            return False

    def _search_tree(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif cur_node.value > value and cur_node.left_child is not None:
            return self._search_tree(value, cur_node.left_child)
        # elif cur_node.value < value and cur_node.right_child is not None:
        #     return self._search_tree(value, cur_node.right_child)
        return False


bt = Binary()
