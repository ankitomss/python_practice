class node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(nd):

    if not nd.next:
        return nd
    dummy = node(0)
    dummy.next = nd

    past, pre, fut = dummy, dummy.next, dummy.next.next
    while pre:
        pre.next, past, pre, fut = past, pre, fut, fut.next if fut else None

    dummy.next.next = None
    return past


def scramble_list(nd):

    slow, fast = nd, nd
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    head2 = slow.next
    slow.next = None
    head1, head2 = nd, reverse_list(head2)
    dummy = node(0)
    temp = dummy
    while head1 or head2:
        if head1:
            dummy.next = head1
            dummy = dummy.next
            head1 = head1.next

        if head2:
            dummy.next = head2
            dummy = dummy.next
            head2 = head2.next

    return temp.next


def print_(nd):
    while nd.next:
        print nd.val
        nd = nd.next

nd = node(1)
nd.next = node(2)
nd.next.next  = node(3)
nd.next.next.next = node(4)
nd.next.next.next.next = node(5)
nd.next.next.next.next.next = node(6)
nd.next.next.next.next.next.next = node(7)

nd = scramble_list(nd)
print_(nd)



