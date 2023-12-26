
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tree_insert(root, node):
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                tree_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                tree_insert(root.right, node)


def in_order_traversal(root):
    res = []
    if root:
        res = in_order_traversal(root.left)
        res.append(root.key)
        res = res + in_order_traversal(root.right)
    return res


def tree_sort(arr):
    if len(arr) == 0:
        return arr

    root = Node(arr[0])
    for i in range(1, len(arr)):
        tree_insert(root, Node(arr[i]))

    return in_order_traversal(root)

# Testing
arr = [5, 4, 3, 2, 1]

print(tree_sort(arr))  # [1, 2, 3, 4, 5]
