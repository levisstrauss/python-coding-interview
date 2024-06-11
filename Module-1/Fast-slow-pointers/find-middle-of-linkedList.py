"""
Given the head of a singly linked list, return the
middle node of the linked list. If the number of nodes
in the linked list is even, there will be two middle nodes,
so return the second one.
"""
"""
Process

Initialize the two pointer to the head

traverse the linkedList while moving slow to 1 and fast to 2 steps

when fast == null, the slow will be in the middle, then return it

"""

"""
Time complexity O(n) because we traversal the array only once

Space complexity: is constant O(1) we are not using any addition array

"""


class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
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


# ------------------- Function to return the middle of the linkedList-------
# Function to find the middle node of the linked list
def get_middle_node(head):
    # Create two pointers, slow and fast ,initially pointing to the head
    slow = head
    fast = head

    # Traverse the linked list until fast reaches at the last node or NULL
    while fast and fast.next:
        # Move slow pointer one step ahead
        slow = slow.next

        # Move fast pointer two steps ahead
        fast = fast.next.next

    # Return the slow pointer
    return slow


# Driver code
def main():
    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i + 1, ".\tLinked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle of the linked list: ",
              get_middle_node(input_linked_list.head).data)
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()
