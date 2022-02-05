# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        normal = []
        n=head
        while n!=None:
            normal.append(n.val)
            n=n.next
        m=0
        l=len(normal)
        for i in range(int(l/2)):
            if normal[i]+normal[l-i-1]>m:
                m=normal[i]+normal[l-i-1]
        return m