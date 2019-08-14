class Node:
    def __init__(self, data=None):
        self.data = data

        self.next = None


class Linkedlst:
    def __init__(self):
        self.head = Node()

    # here v are invoking the Node class.
    # so the g

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            # here next is an attribute of Node
            cur = cur.next
        cur.next = new_node

    def display(self):
        elements = list()
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def search(self, data1):
        cur_node = self.head
        self.head.data = data1
        flag = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_node.data is self.head.data:
                flag = 1
            else:
                pass
            if flag is 1:
                print('found')
            else:
                print('not found')
        # if i in cur_node.data:
        #     print(i)


obj = Linkedlst()
