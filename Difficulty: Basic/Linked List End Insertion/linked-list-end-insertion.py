'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        curr=head
        new=Node(x)
        if head is None:
            return new
        
        while curr.next is not None:
            curr=curr.next
        curr.next=new
        return head