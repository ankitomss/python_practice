import listnode

def partition_list(nd, x):
    if not nd:
        return nd

    dummy = listnode.listnode(0)
    dummy.next = nd
    first, last =  dummy, dummy

    while first or last:
        while first and first.next and first.next.val < x:
            first = first.next

        if not first.next: break
        last = first.next
        while last and last.next and last.next.val >= x:
            last = last.next

        if not last.next: break
        first.next, last.next.next, last.next = last.next, first.next, last.next.next

    return dummy.next


nd = listnode.listnode(1)
nd.next = listnode.listnode(4)
nd.next.next = listnode.listnode(3)
nd.next.next.next = listnode.listnode(2)
nd.next.next.next.next = listnode.listnode(5)
nd.next.next.next.next.next = listnode.listnode(2)

nd = partition_list(nd, 3)
nd.printlist(nd)