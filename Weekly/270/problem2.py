# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextOnes = []
        nextOne = head
        #nextOnes.append(head)
        while True:
            nextOnes.append(nextOne)
            if nextOne.next != None:
                nextOne = nextOne.next
            else:
                break
        print(nextOnes)
        print(len(nextOnes))
        if (len(nextOnes)-1) % 2 == 0:
            midIndex = len(nextOnes) // 2
        else:
            midIndex = (len(nextOnes)) // 2
        print(midIndex)
        if (head == None):
            return None
        if (head.next == None):
            del head
            return None
        copyHead = head
        while (midIndex > 1):
            midIndex -= 1
            head = head.next
        head.next = head.next.next
        return copyHead
    
