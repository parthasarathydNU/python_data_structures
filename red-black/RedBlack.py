from typing import Optional
from Node import Node

class RedBlackTree:
    def __init__(self) -> None:
        self.root = None

    def _dfsHelper(self, parentNode: Optional[Node], newNode: Node) -> Node:
        """
        When we are at any given node, if this node is == to that node, we return the same node
        If this node is lesser than that node, we go left
        If this node is greater than that node, we go right
        If we reach a point where the node is None, we place this node there and return
        We return the inserted Node node at the end
        """

        if parentNode is None:
            return newNode
        
        if parentNode.value == newNode.value:
            return parentNode
        elif parentNode.value < newNode.value:
            parentNode.right = self._dfsHelper(parentNode.right, newNode)
            parentNode.right.parent = parentNode
        else:
            parentNode.left = self._dfsHelper(parentNode.left, newNode)
            parentNode.left.parent = parentNode

        return parentNode

    def _leftRotate(self, pivotNode: Node):
        """
        Imagine you have a parent node and its right child.
        
        In a left rotation, the right child becomes the new parent, 
        and the original parent becomes the left child of the new parent.
        
        The left subtree of the right child (if it exists) 
        becomes the right subtree of the original parent.
        
        Before left rotation
           P (pivot)
            \
             R (new Parent)
            / \
           X   Y
        
        After left rotation   
             R (newParent)
            / \
           P   Y
            \
             X           
        """
        
        newParent = pivotNode.right

        # update child pointers
        pivotNode.right = newParent.left
        newParent.left = pivotNode

        # update parent pointers
        newParent.parent = pivotNode.parent
        pivotNode.parent = newParent

        if pivotNode.right:
            pivotNode.right.parent = pivotNode

        if newParent.parent is None:
            self.root = newParent
        else:
            # Update pivot_node's original parent's child pointer
            if pivotNode == newParent.parent.left:
                newParent.parent.left = newParent
            else:
             newParent.parent.right = newParent



    def _rightRotate(self, pivotNode: Node):
        """
        This is the mirror image of a left rotation.
        The left child becomes the new parent, 
        and the original parent becomes the right child of the new parent.

        Before right rotation
          ogParent
             P (pivot)
            /
           L (new parent)
          / \
         X   Y   

        After Right Rotation
         ogParent
             L (newParent)
            / \
           X   P (pivot Node)
              /
             Y       
        """

        # pick new parent
        newParent = pivotNode.left

        # update child pointers
        pivotNode.left = newParent.right
        newParent.right = pivotNode

        # update parent pointers
        newParent.parent = pivotNode.parent
        pivotNode.parent = newParent
        if pivotNode.left:
            pivotNode.left.parent = pivotNode

        # hadle root case
        if newParent.parent is None:
            self.root = newParent
        else:
            # update pivot node's original parent's child pointer
            if pivotNode == newParent.parent.left:
                newParent.parent.left = newParent
            else:
                newParent.parent.right = newParent




    def _fixViolation(self, insertedNode: Node) -> None:
        """
        This function fixes violations in the red black property after insertion
        """

        """
        # Violation of Red Black Rule
        # A RED node cannot have any child node. 
        # So Until the color of the inserted Node's parent is Red 
        # we have a violation here
        """
        while (insertedNode is not self.root and 
        insertedNode.parent is not None and
        insertedNode.parent.color == "Red"):

            parent = insertedNode.parent
            grandParent = parent.parent
            uncleNode = None # sibbling of the Parent Node
            if grandParent:
                uncleNode = grandParent.left if parent == grandParent.right else grandParent.right
            
            if uncleNode and uncleNode.color == "Red":

                """
                Both parent and uncle are red,  so we make both black
                and make the grand parent red as well
                """
                uncleNode.color = "Black"
                parent.color = "Black"
                grandParent.color = "Red"
                insertedNode = grandParent

            else :
                """
                Uncle is black - check if parent is inner or outer child
                """
                if parent == grandParent.left:
                    """
                    Parent on the left, uncle on the right
                         GP
                    parent  uncle
                    """
                    if insertedNode == parent.left:
                        """  
                                        GP (Black)
                               parent (Red)    uncle (Black)
                        insertedNode (Red)
                        """
                        parent.color = "Black"
                        grandParent.color = "Red"
                        """  
                                         GP (Red)
                               parent (Black)    uncle (Black)
                        insertedNode (Red)
                        """
                        self._rightRotate(grandParent)

                    else:
                        """  
                                GP (black)
                        parent (red)    uncle (black)
                          insertedNode (red)
                        """
                        insertedNode = parent
                        self._leftRotate(parent)
                else:
                    """
                    parent is right child of grand parent
                    Uncle is on the left
                         GP
                    uncle  parent
                    """
                    if insertedNode == parent.left:
                        """
                        left child of parent
                               GP (black)
                        uncle(black)      parent (red)
                                  insertedNode (red)
                        """
                        insertedNode = parent
                        self._rightRotate(parent)
                    else :
                        """
                        righ child of parent
                               GP (black)
                        uncle(black)      parent (red)
                                            insertedNode (red)
                        """ 
                        parent.color = "Black"
                        grandParent.color = "Red"
                        """
                               GP (red)
                        uncle(black)      parent (black)
                                            insertedNode (red)
                        """ 
                        self._leftRotate(grandParent)

        
        if self.root.color == "Red":
            self.root.color = "Black"

    def insertNode(self, val: int, balance: bool = False) -> None:

        node = Node(value=val, color="Red")

        if self.root is None:
            self.root = node
            self.root.color = "Black"
        else:
            self._dfsHelper(self.root, node)
            if balance:
                self._fixViolation(node)

        self.root.color = "Black"
