def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    separator_index = lines.index('')
    rules = lines[:separator_index]
    updates = [list(map(int, line.split(','))) for line in lines[separator_index + 1:]]
    return rules, updates

def build_dependencies(rules):
    dependencies = {}
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if after not in dependencies:
            dependencies[after] = set()
        dependencies[after].add(before)
    return dependencies

def is_update_valid(update, dependencies):
    position = {page: idx for idx, page in enumerate(update)}

    for after, befores in dependencies.items():
        if after in position:
            for before in befores:
                if before in position and position[before] > position[after]:
                    return False
    return True

from collections import defaultdict, deque

def topological_sort(vertices, edges):
    in_degree = {v: 0 for v in vertices}
    adj_list = defaultdict(list)

    for start, end in edges:
        adj_list[start].append(end)
        in_degree[end] += 1

    zero_in_degree_queue = deque([v for v in vertices if in_degree[v] == 0])
    top_order = []

    while zero_in_degree_queue:
        vertex = zero_in_degree_queue.popleft()
        top_order.append(vertex)

        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)

    return top_order if len(top_order) == len(vertices) else []

def reorder_update(update, dependencies):
    page_set = set(update)
    filtered_rules = [(before, after) for after, befores in dependencies.items() for before in befores if before in page_set and after in page_set]
    return topological_sort(update, filtered_rules)

def find_middle_page(update):
    n = len(update)
    return update[n // 2]

def main(file_path):
    rules, updates = read_input(file_path)
    dependencies = build_dependencies(rules)
    
    valid_updates = [update for update in updates if is_update_valid(update, dependencies)]
    middle_pages_valid = [find_middle_page(update) for update in valid_updates]
    result_valid = sum(middle_pages_valid)
    
    print(f"The sum of the middle pages from correctly ordered updates is: {result_valid}")

    # Part 2 - Reorder incorrectly ordered updates and find their middle pages
    invalid_updates = [update for update in updates if not is_update_valid(update, dependencies)]
    reordered_updates = [reorder_update(update, dependencies) for update in invalid_updates]
    middle_pages_reordered = [find_middle_page(update) for update in reordered_updates]
    result_invalid = sum(middle_pages_reordered)
    
    print(f"The sum of the middle pages from reordered incorrect updates is: {result_invalid}")

# Specify the path to your input file
file_path = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day05/input.txt'
main(file_path)
