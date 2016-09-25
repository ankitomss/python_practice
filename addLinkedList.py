class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def add(a, b):
    if not a and not b:
        return 0, None

    carry, node=add(a.next, b.next)
    newnode=ListNode((a.val+b.val+carry)%10)
    newnode.next=node
    return (a.val+b.val+carry)/10, newnode


a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)

b=ListNode(3)
b.next=ListNode(4)
b.next.next=ListNode(5)

carry, result=add(a,b)
while result:
    print result.val
    result=result.next


# def addList(ListNode a, ListNode b):
#     temp1, temp2=a, b
#     count1, count2=0,0
#     while temp1 or temp2:
#         if temp1:
#             temp1=temp1.next
#             count1+=1
#         if temp2:
#             temp2=temp2.next
#             count2+=1
#
#
#     if count1==count2:
#         carry, result=add(a, b)
#     elif count1>count2:
#         diff=count1-count2
#         temp1=a
#         while (diff):
#             diff-=1
#             temp1=temp1.next
#
#         carry, result=add(temp1, b)
#     elif count2>count1:
#         diff=count2-count1
#         temp2=b
#         while (diff):
#             diff-=1
#             temp2=temp2.next
#         carry, result=add(a, temp2)
#         if carry: addcarry()





