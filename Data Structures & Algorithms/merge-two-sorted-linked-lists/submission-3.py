# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        current1=list1
        current2=list2
        while current1 or current2:
            if current1 and current2:
                if current1.val <= current2.val:
                    nodes.append(current1)
                    current1 = current1.next
                else:
                    nodes.append(current2)
                    current2 = current2.next
            elif current1:
                nodes.append(current1)
                current1 = current1.next

            else: 
                nodes.append(current2)
                current2 = current2.next
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if nodes:
            nodes[-1].next = None  
            return nodes[0]        

        return None

        