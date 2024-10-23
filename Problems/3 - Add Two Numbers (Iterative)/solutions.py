from typing import Optional, List
from ListNode import ListNode

class Solution():
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Psuedocode:
        1. Initialize a dummy head for the result list.
        2. Initialize a current pointer to the dummy head.
        3. Initialize a carry variable to 0.
        4. Traverse both lists until both are exhausted.
        5. Add the values of the current nodes along with the carry.
        6. Update the carry for the next iteration.
        7. Append the digit to the result list.
        8. Move to the next nodes.

        Time complexity: O(max(m, n))
        Space complexity: O(max(m, n))
        Algorithm: Iterative
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy_head.next
