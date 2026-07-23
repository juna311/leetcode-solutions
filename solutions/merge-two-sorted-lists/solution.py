# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        currentMerged = dummy
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val <= current2.val:
                currentMerged.next = current1 
                current1 = current1.next
                currentMerged = currentMerged.next
            else: 
                currentMerged.next = current2
                current2 = current2.next
                currentMerged = currentMerged.next
        if current1: 
            currentMerged.next = current1
        else: currentMerged.next = current2
        return dummy.next
        