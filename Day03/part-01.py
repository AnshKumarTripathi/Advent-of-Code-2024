import re

def extract_and_validate_instructions(memory):
    products = []
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(memory)
    
    for match in matches:
        X = int(match[0])
        Y = int(match[1])

        if 0 < X < 1000 and 0 < Y < 1000:
            product = X * Y
            products.append(product)
    
    return products

def read_memory_from_file(filename):
    with open(filename, 'r') as file:
        memory = file.read().strip()
    return memory

def main():
    filename = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day03/input.txt' 

    memory = read_memory_from_file(filename)
    
    products = extract_and_validate_instructions(memory)

    total_sum = sum(products)

    print("Total sum of valid multiplications:", total_sum)

main()
