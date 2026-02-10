# Given the head of a singly linked list, reverse the list and return its head.
# Implement a function reverseList that takes the head of the linked list as input and returns the new head of the reversed list.
# Refer to the ListNode class/struct and do not comment it out.

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev


head = ListNode(1, ListNode(2))
reversed_head = reverse_list(head)
print(reversed_head.val)
print(reversed_head.next.val)


