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

def main(file_path):
    rules, updates = read_input(file_path)
    dependencies = build_dependencies(rules)
    
    valid_updates = [update for update in updates if is_update_valid(update, dependencies)]
    middle_pages = [update[len(update) // 2] for update in valid_updates]
    result = sum(middle_pages)
    
    print(f"The sum of the middle pages from correctly ordered updates is: {result}")

# Specify the path to your input file
file_path = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day05/input.txt'
main(file_path)
