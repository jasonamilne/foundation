from solutions import Solution
from solutions import Solution
from ListNode import ListNode
import pytest

@pytest.fixture
def solution():
    return Solution()

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_addTwoNumbers(solution):
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7, 0, 8]

    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0]

    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

def test_addTwoNumbers_edge_cases(solution):
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([1, 2, 3])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [1, 2, 3]

    l1 = list_to_linkedlist([1, 2, 3])
    l2 = list_to_linkedlist([])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [1, 2, 3]
