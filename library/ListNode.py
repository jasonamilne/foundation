class ListNode():
    """
    A class to represent a node in a singly linked list.
    Attributes:
        val (int): The value stored in the node.
        next (ListNode): The next node in the linked list (default is None).
    Runtime:
        O(1) for initialization, accessing a node, inserting at the beginning, deleting from the beginning.
        O(n) for iteration, searching, inserting in the middle/end, deleting in the middle/end, 
        deleting by value, reversing, finding middle/nth node, cycle detection/removal, 
        merging sorted lists, finding intersection, removing nth node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
