class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


# 🔹 Helper: create linked list
def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    
    return head


# 🔹 Helper: print linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# 🔹 MAIN TEST
arr = [0, 1, 2, 3]

head = create_linked_list(arr)

print("Original List:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed List:")
print_linked_list(reversed_head)