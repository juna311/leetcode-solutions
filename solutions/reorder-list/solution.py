# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head
        arr = []
        while current is not None:
            arr.append(current)
            current = current.next

        left = 1
        right = len(arr) - 1
        current = head
        while left < right:
            current.next = arr[right]
            current = current.next
            current.next = arr[left]
            current = arr[left]
            right -= 1
            left += 1
            if right < left:
                current.next = None
            elif right == left:
                current.next = arr[right]
                current = current.next
                current.next = None
        return

                
            
