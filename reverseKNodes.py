class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        current=head
        prev=None
        count=0
        while current and count<k:
            next=current.next
            current.next=prev
            prev=current
            current=next
            count+=1

        if next:
            head.next=self.reverseKGroup(next, k)

        return prev


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

temp=Solution().reverseKGroup(head, 3)
while temp:
    print temp.val
    temp=temp.next
