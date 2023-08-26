                                              #LINKED LISTS QUESTIONS SOLVED

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 23. Merge k Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge(lists[i],lists[i + interval])

            interval *=2
        
        return lists[0]

    def merge(self,l1,l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                l1.next = self.merge(l1.next,l2)
                return l1
            else:
                l2.next = self.merge(l1,l2.next)
                return l2
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 237. Delete Node in a Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        return 

'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 203. Remove Linked List Elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(next=head)
        prev, curr = node, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return node.next

'''--------------------------------------------------------------------------------------------'''
