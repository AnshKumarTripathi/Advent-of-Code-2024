def calculate_total_distance(left_list, right_list):
    # Step 1: Sort both lists
    left_list.sort()
    right_list.sort()
    
    print("Sorted left_list:", left_list)   # Debugging
    print("Sorted right_list:", right_list)  # Debugging
    
    total_distance = 0
    
    # Step 2: Pair the numbers and calculate distances
    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        total_distance += distance
        print(f"Pair: ({left}, {right}), Distance: {distance}")  # Debugging
    
    return total_distance

def read_lists_from_file(filename):
    left_list = []
    right_list = []
    row_count = 0
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            # Ensure line is not empty and has two columns
            if line.strip() and len(line.split()) == 2:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
                row_count += 1
    
    print("Number of rows in the dataset (excluding the header):", row_count)  # Debugging
    return left_list, right_list, row_count

# Read lists from the text file
left_list, right_list, row_count = read_lists_from_file('input.txt')

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
print("Total Distance:", total_distance)
