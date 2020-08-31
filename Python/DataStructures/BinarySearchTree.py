class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value, cur_node.left_child)

        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value, cur_node.right_child)

        else:
            print(value, "Value already in tree")

    def print_tree(self):
        print("here")
        if self.root!=None:
            print("???")
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        print("what ", cur_node)
        if cur_node!=None:
            print("=")
            self._print_tree(cur_node.left_child)
            print("==")
            print(str(cur_node.value))
            print("===")
            self._print_tree(cur_node.right_child)

def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree

def fill_tree_custom(tree):
    ary = [6, 9, 3, 10, 7, 2, 4]
    for i in range(len(ary)):
        tree.insert(ary[i])
    return tree


tree = BST()
tree = fill_tree_custom(tree)

tree.print_tree()


