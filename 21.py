from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return result.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
obj = Solution()
merged_list = obj.mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val)
    merged_list = merged_list.next
