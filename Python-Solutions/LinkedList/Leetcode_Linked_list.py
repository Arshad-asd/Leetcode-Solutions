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

# QUESTION NO: 2. Add Two Numbers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next 
    
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO: 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 2236. Root Equals Sum of Children
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False
'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 83. Remove Duplicates from Sorted List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 148. Sort List
#METHOD 1: Merge sort used O(n log n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        middle = self.find_middle(head)

        # Split the linked list into two halves
        left_half = head
        right_half = middle.next
        middle.next = None

        # Recursively sort both halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach the remaining nodes from either left or right
        current.next = left or right

        return dummy.next

#METHOD 2: buble sort: O(n) not use full for large data set
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = head
        while first:
            current = head
            while current and current.next :
                if current.val >= current.next.val:
                    temp = current.next.val
                    current.next.val = current.val
                    current.val = temp
                    current = current.next
                else:
                    current = current.next
            first = first.next
        return head
'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 1290. Convert Binary Number in a Linked List to Integer
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        result = 0
        while current:
            result = result * 2 + current.val
            current = current.next
        return result
'''--------------------------------------------------------------------------------------------'''

# QUESTION NO:19. Remove Nth Node From End of List

class Solution:
    def find_len(self,head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         index = 0
         length = self.find_len(head)
         current = head 
         while current and index < length-n:
             prev = current 
             current = current.next
             index += 1
         if current is None:
             return head
         elif index == 0:
             head = head.next
         else:
             prev.next = current.next
         return head
'''--------------------------------------------------------------------------------------------'''
# QUESTION NO: 147. Insertion Sort List
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(float('-inf'))
        dummy.next = head
        last_sorted = head
        
        while last_sorted.next:
            if last_sorted.next.val < last_sorted.val:
                prev = dummy
                while prev.next.val < last_sorted.next.val:
                    prev = prev.next
                
                temp = last_sorted.next
                last_sorted.next = temp.next

                temp.next = prev.next
                prev.next = temp
            else:
                last_sorted = last_sorted.next
        
        return dummy.next

# QUESTION NO 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False