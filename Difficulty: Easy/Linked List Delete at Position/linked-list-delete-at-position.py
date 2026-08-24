''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        new=head
        if x==1:
            return new.next
        for i in range(x-2):
            new=new.next
        new.next=new.next.next
        return head