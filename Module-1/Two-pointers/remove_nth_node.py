"""
Problem statement
given a linkedlist, we have to remove the given element starting
counting from the end of the linkedlist

"""

# Thought Process
"""
1- Set two pointers, right and left at the head of the linkedlist
2- Move the right pointer m steps forward
3- Move both forward until right reaches the last node. At this point
   the left pointer will be pointing the node behind the nth last node
4-  Relink the left node to node next to left's next node
5- Return the head of the linkedlist 
"""


# Create a linkedList node
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create a linkedlist
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


# Print a linkedlist
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value

        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")


# Solution
# time complexity O(n) where n is the number of nodes
# space complexity is O(1) using constant space to store two pointers
def remove_nth_last_node(head, n):
    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for i in range(n):
        right = right.next

    # Removal of the head node.
    if not right:
        return head.next

    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next element of left.
    left.next = left.next.next

    return head


# Driver code
def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76],
             [288, 224, 275, 390, 4, 383, 330, 60, 193],
             [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 9, 11]

    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i + 1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print()
        print("n = ", n[i])
        result = remove_nth_last_node(input_linked_list.head, n[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print()
        print("-" * 100)


if __name__ == '__main__':
    main()
