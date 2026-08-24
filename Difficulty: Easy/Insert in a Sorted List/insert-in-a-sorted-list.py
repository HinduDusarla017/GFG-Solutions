'''Definition of a Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

class Solution:
    def sortedInsert(self, head, key):
        # code here
        new=Node(key)
        if head is None or key<head.data:
            new.next=head
            return new
        curr=head
        while curr.next is not None and curr.next.data<key:
            curr=curr.next
        new.next=curr.next
        curr.next=new
        return head
        