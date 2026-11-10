class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next = None

def linkedlist_lastname_operations():
    # Step 1: Define Node structure and initialize Head
    head = None
    target_name = ['A', 'B', 'E', 'L', 'L', 'A']

    print("=== Step 2: Insertion at Tail (Add each letter) ===")
    for letter in target_name:
        new_node = Node(letter)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print(f"Appended '{letter}' to Linked List.")

    print("\n=== Step 3: Deletion from Head (Remove each letter until empty) ===")
    while head is not None:
        removed_letter = head.letter
        head = head.next
        print(f"Deleted node containing '{removed_letter}' from Linked List.")

    print("\nLinked List is now empty.")

if __name__ == "__main__":
    linkedlist_lastname_operations()