# Day 15: Linked List

class Node:
    def __init__(self, data):
        """
        Initialize a node object with the given data value.
        Attributes:
            data: The value stored in the node.
            next: A pointer to the next node, initialized as None.
        """
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        """
        Prints all the elements of the linked list.
        Args:
            head: The head node of the linked list.
        """
        # Traverse the list starting from the head
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        """
        Inserts a new node with the given data at the end of the linked list.
        Args:
            head: The head node of the linked list.
            data: The data value for the new node.
        Returns:
            The head node of the updated linked list.
        """
        new_node = Node(data)

        # If the list is empty, the new node becomes the head
        if head is None:
            return new_node

        # Traverse to the end of the list
        current = head
        while current.next:
            current = current.next

        # Link the new node to the end of the list
        current.next = new_node
        return head


if __name__ == "__main__":
    # Create an instance of the Solution class
    mylist = Solution()
    head = None  # Initialize the linked list as empty

    T = int(input())  # Read the number of elements to insert into the linked list

    for _ in range(T):
        data = int(input())  # Read the data value for each node
        head = mylist.insert(head, data)  # Insert the data into the linked list

    mylist.display(head)  # Display the elements of the linked list
