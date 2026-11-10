from collections import deque

def queue_lastname_operations():
    # Step 1: Initialization
    queue = deque()
    target_name = ['A', 'B', 'E', 'L', 'L', 'A']

    print("=== Step 2: Enqueue Operations (Add each letter) ===")
    for letter in target_name:
        queue.append(letter)
        print(f"Enqueued '{letter}' into Queue.")

    print("\n=== Step 3: Dequeue Operations (Remove each letter until empty) ===")
    while len(queue) > 0:
        removed_letter = queue.popleft()
        print(f"Dequeued '{removed_letter}' from Queue.")

    print("\nQueue is now empty.")

if __name__ == "__main__":
    queue_lastname_operations()