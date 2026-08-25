""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        # code here
        if head==None or head.next is None:
            return None
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head