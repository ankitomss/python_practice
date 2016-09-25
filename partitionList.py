class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution(object):
    def partition(self, head, x):
        temp, second=head, head
        count=0
        while temp!=None:
            if temp.val < x:
                count+=1
                second=second.next
            temp=temp.next

        first=head
        while second!=None:
            while first and first.val <x:
                first=first.next
            while second and second.val >= x:
                second=second.next
            if not second: break
            temp, first.val, second.val=first.val, second.val, temp
            

        temp=head
        while temp!=None:
            print temp.val
            temp=temp.next


#1->4->3->2->5->2
head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(2)
Solution().partition(head,3)