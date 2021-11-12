class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

        self.preorder = []
        self.inorder = []
        self.posorder = []

    def set_order(self, node=None):
        if node is None:
            node = self.root
        self.preorder.append(node.data)
        if node.left:
            self.set_order(node.left)
        self.inorder.append(node.data)
        if node.right:
            self.set_order(node.right)
        self.posorder.append(node.data)


class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)



if __name__=='__main__':
    cases_qty = int(input())

    for i in range(0, cases_qty):
        numbers_qty = input()
        numbers = list(map(int, input().split()))

        tree = BinarySearchTree()
        for item in numbers:
            tree.insert(item)

        tree.set_order()

        print(''.join(['Case ', str(i+1), ':']))
        print('Pre.:', *tree.preorder)
        print('In..:', *tree.inorder)
        print('Post:', *tree.posorder)
        print('')