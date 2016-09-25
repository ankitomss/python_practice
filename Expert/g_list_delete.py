class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_delete(ls, val):
    dummy = ListNode(0)
    dummy.next = ls
    ls = dummy
    while ls and ls.next:
        if ls.next.val > val:
            ls.next = ls.next.next
        ls = ls.next

    return dummy.next

ls = ListNode(3)
ls.next = ListNode(4)
ls.next.next = ListNode(5)
ls.next.next.next = ListNode(6)

ret = list_delete(ls, 5)
while ret and ret.next:
    print ret.val
    ret = ret.next
