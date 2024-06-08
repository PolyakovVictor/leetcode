from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        rem = 0
        while l1 or l2 or rem:

            if l1:
                rem += l1.val
                l1 = l1.next
            if l2:
                rem += l2.val
                l2 = l2.next
            cur.next = ListNode(rem % 10)
            rem //= 10
            cur = cur.next
        return head.next


cls = Solution()
l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
result = cls.addTwoNumbers(l1=l1, l2=l2)


while result:
    print(result.val, end=" ")
    result = result.next
