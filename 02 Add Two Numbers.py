# https://leetcode.com/problems/two-sum/
# ref: https://www.youtube.com/watch?v=wgFPrzTjm7s

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def two_sum(self, l1, l2) -> ListNode:
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        # New digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        # Update pointers
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

l1 = [11, 15, 6, 2, 7]
l2 = 9
two_sum(two_sum, l1, l2)
