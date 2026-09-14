# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        current=head
        while current:
            nodes.append(current)
            current=current.next
        for i in range(len(nodes)-1,0,-1):
            nodes[i].next=nodes[i-1]
        if nodes:
            nodes[0].next=None
            return nodes[-1]

        return None
        