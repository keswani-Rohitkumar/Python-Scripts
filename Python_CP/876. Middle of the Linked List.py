# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        le = 0
        while temp != None:
            le+=1
            temp = temp.next

        mid = le //2
        l = 0
        while l < mid:
            head = head.next
            l +=1
        return head