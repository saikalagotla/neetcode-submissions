# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(None)
        pointer = head
        i = 0
        while list1 and list2:
            pointer.next = ListNode(None)
            if(list1.val < list2.val):
                pointer.next.val = list1.val
                list1 = list1.next
            else:
                pointer.next.val = list2.val
                list2 = list2.next

            pointer = pointer.next

        while list1:
            pointer.next = ListNode(None)
            pointer.next.val = list1.val
            pointer = pointer.next
            list1 = list1.next

        while list2:
            pointer.next = ListNode(None)
            pointer.next.val = list2.val
            pointer = pointer.next
            list2 = list2.next

        return head.next
