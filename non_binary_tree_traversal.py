class Node:

    def __init__(self, n, data):
        self._data = data
        self._child_nodes = n*[None]


def print_tree_depth_first_search(node):
    if node is not None:
        child_nodes_number = len(node._child_nodes)

        for i in range(child_nodes_number-1):
            print_tree_depth_first_search(node._child_nodes[i])

        print(node._data)

        print_tree_depth_first_search(
            node._child_nodes[child_nodes_number - 1])
    else:
        return


def non_binary_tree_nodes_count(node):
    if node is not None:
        child_nodes_number = len(node._child_nodes)

        nodes_count = 0
        for i in range(child_nodes_number):
            nodes_count += non_binary_tree_nodes_count(node._child_nodes[i])

        nodes_count += 1

        return nodes_count
    else:
        return 0


def count_leaf_nodes(node):
    count = 0
    if node is not None:

        children_number = len(node._child_nodes)

        # check if it is leaf. Leaf if all children are None
        isLeafNode = True

        for i in range(children_number):

            # check if it is non leaf, then call recursively count_leaf_nodes until we meet leaf elements.

            if node._child_nodes[i] is not None:
                isLeafNode = False
                count += count_leaf_nodes(node._child_nodes[i])

        if isLeafNode:
            count += 1

        return count

    else:
        return 0


# Create the following tree
        #          5
        #       /  |  \
        #      3   4   6
        #    / | \
        #   1  2  7

n = 3
node = Node(n, 5)
node._child_nodes[0] = Node(n, 3)
node._child_nodes[1] = Node(n, 4)
node._child_nodes[2] = Node(n, 6)
node._child_nodes[0]._child_nodes[0] = Node(n, 1)
node._child_nodes[0]._child_nodes[1] = Node(n, 2)
node._child_nodes[0]._child_nodes[2] = Node(n, 7)


print_tree_depth_first_search(node)

nodes_count = non_binary_tree_nodes_count(node)
print(nodes_count)

leaf_nodes_count = count_leaf_nodes(node)
print(f'Leaf nodes count: {leaf_nodes_count}')
