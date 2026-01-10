class LinkedList:
    """A class representing a linear collection of data elements called nodes."""
    class Node:
        """Represents an individual element in the linked list."""
        def __init__(self, element):
            # The data stored in this node
            self.element = element
            # Placeholder for the reference to the next node
            self.next = None
    def __init__(self):
        self.length = 0
        self.head = None
    def is_empty(self):
        """Returns True if the list contains no nodes, otherwise False."""
        return self.length == 0
    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            # Start the search at the beginning of the list
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
    def remove(self, element):
        # We start with None because there is no node before the head
        previous_node = None
        current_node = self.head
        # Loop until we reach the end of the list OR find the element
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            # Skip over current_node by linking previous directly to current's next
            previous_node.next = current_node.next
        else:
            # If previous_node is None, we are removing the head
            self.head = current_node.next
        self.length -= 1

# Create an instance of the LinkedList
my_list = LinkedList()

# Check if the newly created list is empty
print(my_list.is_empty())
# New code: Add elements and check state
my_list.add(1)
my_list.add(2)

print(my_list.is_empty())  # Should now print: False
print(my_list.length)      # Should print: 2
# New code: Remove an element and check the updated length
my_list.remove(1)
print(my_list.length)  # Should now print: 1
