from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        result = []

        while l1 or l2:
            print(l1.val, l1.val)
            if l1.val:
                num1 += str(l1.val)
                l1 = l1.next
            if l2.val:
                num2 += str(l2.val)
                l2 = l2.next


        num3 = str(int(num1) + int(num2))
        print(num3)
        for i in range(len(num3)):
            result.append(num3[:i])
        return result


cls = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(cls.addTwoNumbers(l1=l1, l2=l2))
