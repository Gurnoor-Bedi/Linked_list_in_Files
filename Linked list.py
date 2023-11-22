class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    # Append a new node with the given data to the end of the linked list
    new_node = Node(data)
    if self.head is None:
      # If the list is empty, set the new node as the head
      self.head = new_node
      return
    # Traverse to the end of the list and add the new node
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def display(self):
    # Display the elements of the linked list
    current = self.head
    while current:
      print(current.data, end="->")
      current = current.next
    print("None")

  def insert_at_position(self, data, position):
    # Insert a new node with the given data at the specified position
    new_node = Node(data)
    if position == 0:
      # If position is 0, insert at the beginning
      new_node.next = self.head
      self.head = new_node
      return
    # Traverse to the specified position and perform the insertion
    current = self.head
    for i in range(position - 1):
      if current is None:
        raise IndexError("Index out of range.")
      current = current.next
    new_node.next = current.next
    current.next = new_node

  def delete(self, data):
    # Delete the first occurrence of a node with the given data
    if self.head is None:
      return
    if self.head.data == data:
      # If the data to be deleted is in the head, update the head
      self.head = self.head.next
      return
    # Traverse the list to find and delete the node
    current = self.head
    while current.next:
      if current.next.data == data:
        current.next = current.next.next
        return
      current = current.next

  def length(self):
    # Calculate the length of the linked list
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  @classmethod
  def from_file(cls, filename):
    # Create a linked list and populate it with data from a file
    Linked_List = cls()
    with open(filename, "r") as file:
      for line in file:
        data = line.strip()
        Linked_List.append(data)
    return Linked_List

# Create a linked list, append elements, and display it
sports = LinkedList()
sports.append("basketball")
sports.append("formula1")
sports.append("football")
sports.append("sprint")
sports.display()

# Write the contents of the linked list to a file
with open("Linked_List.txt", "w") as file:
  current = sports.head
  while current:
    file.write(str(current.data) + "\n")
    current = current.next
print("Contents of linked list:")

# Read the contents of the file and print them
with open("Linked_List.txt", "r") as file:
  content = file.read()
  print(content)

# Create a new linked list from the file and display it
new_list = LinkedList.from_file("Linked_List.txt")
print("Linked List accepted from a file")
new_list.display()
