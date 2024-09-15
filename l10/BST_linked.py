"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author: Aliyya Wasiq
ID:     169023106
Email:  wasi3106@mylaurier.ca
__updated__ = "2023-08-16"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import copy, deepcopy


class BST:
    """
    A linked BST class.
    """

    def are_siblings(self, v1, v2):
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are siblings.
        Nodes are siblings if they have the same parent.
        Use: b = source.are_siblings(v1, v2)
        -------------------------------------------------------
        Parameters:
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            siblings - True if the nodes containing v1 and v2 are siblings,
                False otherwise.
        -------------------------------------------------------
        """
        siblings = self._are_siblings_aux(self._root, v1, v2)
        return siblings

    def _are_siblings_aux(self, parent, v1, v2):
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are siblings.
        Nodes are siblings if they have the same parent.
        Use: siblings = self._are_siblings_aux(parent, v1, v2)
        -------------------------------------------------------
        Parameters:
            parent - a potential parent of nodes containing v1 and v2 (_BST_Node)
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            siblings - True if the nodes containing v1 and v2 are siblings,
                False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return

    def longest_path(self):
        """
        ---------------------------------------------------------
        Returns the values in the longest path of source. If there are multiple
        paths of the same maximum length, return the leftmost path.
        Returns an empty list if source is empty.
        Use: path = source.longest_path()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            path - a list of values of the longest path from 
                root to the leaves of source (list of *)
        ---------------------------------------------------------
        """
        path = self._longest_path_aux(self._root)
        return path

    def _longest_path_aux(self, node):
        """
        ---------------------------------------------------------
        Returns a list of the values in the longest path from node to the
        leaves of self.
        Private auxiliary method for max_path.
        Use: path = self._longest_path_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            path - a list of the values in the longest path from node
                to the leaves of self (list of *)
        ---------------------------------------------------------
        """

        # Your code here

        return

    def furthest(self):
        """
        -------------------------------------------------------
        Returns the values of the left-most and right-most nodes in source.
        Use: values = source.furthest()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            values - the values in the left-most and right-most nodes,
                in that order, an empty list if the bst is empty (list of *)
        -------------------------------------------------------
        """

        # Your code here

        return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into node,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder. a contains the contents of
        node and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target list of data (list of ?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder. a contains the contents of
        node and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._postorder_aux(self._root, a)
        return a

    def _postorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in postorder. a contains the contents of
        node and its children in postorder.
        Private recursive operation called only by postorder.
        Use: self._postorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left, a)
            self._postorder_aux(node._right, a)
            a.append(deepcopy(node._value))
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []

        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                values.append(deepcopy(node._value))

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
        return values

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node
                # yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)


class _BST_Node:
    """
    A linked BST Node class.
    """

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node. _height is 1 plus
        the maximum of the node's (up to) two child heights.
        Use: node._update_height()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​​‌​‌‌​‌​​​​​‌​:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
