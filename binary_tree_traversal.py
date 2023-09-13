class Node:

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def add(self, data):
        if self._data is None:
            self._data = data
        else:
            if self._data > data:
                if self._left is None:
                    self._left = Node(data)
                else:
                    self._left.add(data)

            elif self._data < data:
                if self._right is None:
                    self._right = Node(data)
                else:
                    self._right.add(data)


def print_tree_inorder_traversal(node):
    if node is not None:
        print_tree_inorder_traversal(node._left)

        print(node._data)

        print_tree_inorder_traversal(node._right)
    else:
        return


def print_tree_preorder_traversal(node):
    if node is not None:

        print(node._data)

        print_tree_preorder_traversal(node._left)

        print_tree_preorder_traversal(node._right)
    else:
        return


def print_tree_postorder_traversal(node):
    if node is not None:

        print_tree_postorder_traversal(node._left)

        print_tree_postorder_traversal(node._right)

        print(node._data)
    else:
        return


def print_tree_levelorder_traversal(node):
    if node is not None:
        print(node._data)

        print_tree_postorder_traversal(node._left)

        print_tree_postorder_traversal(node._right)

    else:
        return


def binary_tree_nodes_count(node):
    if node is not None:
        left_nodes_count = binary_tree_nodes_count(node._left)
        right_nodes_count = binary_tree_nodes_count(node._right)

        total_nodes_count = left_nodes_count + right_nodes_count + 1

        return total_nodes_count
    else:
        return 0


def count_leaf_nodes(node):
    count = 0
    if node is not None:
        # check if it is leaf. Leaf if both children are None
        if node._left is None and node._right is None:
            count += 1
            return count
        # check if it is non leaf, then call recursively count_leaf_nodes until we meet leaf elements.
        else:
            count += count_leaf_nodes(node._left)
            count += count_leaf_nodes(node._right)
            return count

    else:
        return 0


def count_non_leaf_nodes(node):
    count = 0
    if node is not None:

        if node._left is None and node._right is None:
            return 0

        else:
            left_count = count_non_leaf_nodes(node._left)
            right_count = count_non_leaf_nodes(node._right)

            total_count = left_count + right_count + 1

            return total_count

    else:
        return 0

# Create the following tree
        #        5
        #      /  \
        #     3    7
        #    / \
        #   1   4


node = Node(5)
node.add(3)
node.add(7)
node.add(1)
node.add(4)


print_tree_inorder_traversal(node)

print("---")

print_tree_preorder_traversal(node)

print("---")

print_tree_postorder_traversal(node)

# total_nodes_count = binary_tree_nodes_count(node)
# print(total_nodes_count)

# non_leaf_nodes_count = count_non_leaf_nodes(node)
# print(f'Non Leaf nodes count: {non_leaf_nodes_count}')

# leaf_nodes_count = count_leaf_nodes(node)
# print(f'Leaf nodes count: {leaf_nodes_count}')
