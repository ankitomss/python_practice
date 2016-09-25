class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head, k):

    if not head.next:
        return head, head

    node, last=reverse(head.next, k)
    last.next=head
    head.next=None

    return node, head

def reversekgroup(head, k):

    if not head:
        return None

    current, prev=head, None
    count=0

    while current and count < k:
        next=current.next
        current.next=prev
        prev=current
        current=next
        count+=1

    if next:
        head.next=reversekgroup(next, k)

    return prev

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)

head, last=reverse(head, 2)
while head:
    print head.val
    head=head.next


