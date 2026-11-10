class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def stack_lastname_operations():
    # Step 1: Initialization
    stack = Stack()
    target_name = ['A', 'B', 'E', 'L', 'L', 'A']

    print("=== Step 2: Push Operations (Add each letter) ===")
    for letter in target_name:
        stack.push(letter)
        print(f"Pushed '{letter}' onto Stack. Top element: {stack.peek()}")

    print("\n=== Step 3: Pop Operations (Remove each letter until empty) ===")
    while not stack.is_empty():
        removed_letter = stack.pop()
        print(f"Popped '{removed_letter}' from Stack.")

    print("\nStack is now empty.")

if __name__ == "__main__":
    stack_lastname_operations()