def array_lastname_operations():
    # Step 1: Initialization
    capacity = 6
    letters = [None] * capacity
    target_name = ['A', 'B', 'E', 'L', 'L', 'A']
    size = 0

    print("=== Step 2: Insertion (Add each letter of ABELLA) ===")
    for letter in target_name:
        letters[size] = letter
        size += 1
        current_slice = ", ".join(repr(l) for l in letters[:size])
        print(f"Inserted '{letter}' into Array. Current Array: [{current_slice}]")

    print("\n=== Step 3: Deletion (Remove each letter until empty) ===")
    while size > 0:
        removed_letter = letters[0]

        # Shift remaining elements left
        for i in range(size - 1):
            letters[i] = letters[i + 1]

        letters[size - 1] = None  # Clear out the last slot
        size -= 1

        if size > 0:
            remaining_slice = ", ".join(repr(l) for l in letters[:size])
            print(f"Removed '{removed_letter}' from Array. Remaining Array: [{remaining_slice}]")
        else:
            print(f"Removed '{removed_letter}' from Array. Remaining Array: []")

    print("\nArray is now empty.")


if __name__ == "__main__":
    array_lastname_operations()