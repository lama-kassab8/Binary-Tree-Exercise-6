class Node:
    def __init__(self, data):
        self.data= data
        self.right= None
        self.left= None

class BST:
    def __init__(self):
        self.root= None

    def range_search(self, node,low, high, result):
        if node is None: # if the tree is empty or the method tries to reach beyond the leaves, it will stop
            return 
        if low < node.data: # explore the left subtree only if there's a chance of finding values that are greater than low:
            self.range_search(node.left, low, high, result) # keep recursively calling the function until the condition is no longer valid
        if high> node.data: # explore the right subtree only if there's a chance of finding values less than high:
            self.range_search(node.right, low, high, result) # keep recursively calling the function until the condition is no longer valid  
        if low <= node.data <= high: # as long as current node's value is the same as the values of low and high or greater than the value of low or less than the value of high:
            result.append(node.data) # append all the nodes in this range in the list "results"
        

# test run
tree = BST()
tree.root = Node(40)
tree.root.left = Node(20)
tree.root.right = Node(60)
tree.root.left.left = Node(10)
tree.root.left.right = Node(30)
tree.root.right.left = Node(50)
tree.root.right.right = Node(70)

result = []
tree.range_search(tree.root, 25, 65, result)
print(result)  # output: [30, 40, 50, 60]
