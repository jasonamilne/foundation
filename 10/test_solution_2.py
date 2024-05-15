from solution import Solution, ListNode
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_addTwoNumbers_with_carry_over(solution):
    """Test when the sum has carry over to next digit"""
    l1 = ListNode.create_linked_list([2, 4, 3])
    l2 = ListNode.create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert ListNode.linked_list_to_list(result) == [7, 0, 8]

def test_addTwoNumbers_with_zero_values(solution):
    """Test when both lists represent the number zero"""
    l1 = ListNode.create_linked_list([0])
    l2 = ListNode.create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert ListNode.linked_list_to_list(result) == [0]

def test_addTwoNumbers_with_different_lengths(solution):
    """Test when the lists have different lengths"""
    l1 = ListNode.create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode.create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert ListNode.linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
