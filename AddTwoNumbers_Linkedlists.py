# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1!=None:
            s1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            s2+=str(l2.val)
            l2=l2.next
        s1=int(s1[::-1])
        s2=int(s2[::-1])
        res=str((s1)+(s2))[::-1]
        final=ListNode(0)
        tmp=final
        for i in res:
            tmp.next=ListNode(int(i))
            tmp=tmp.next
        return final.next