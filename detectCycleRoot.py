class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        slow, fast = head, head
        if fast.next == slow or fast.next.next == slow: return slow

        flag = 0
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = 1
                break

        if flag == 0: return None
        count = 1
        fast = fast.next
        while slow != fast:
            fast = fast.next
            count += 1
        slow, fast = head, head
        while count:
            fast = fast.next
            count -= 1

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

