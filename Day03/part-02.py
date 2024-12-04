import re

def extract_and_validate_instructions(memory):
    products = []
    mul_enabled = True
    
    pattern = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))")
    matches = pattern.finditer(memory)
    
    for match in matches:
        mul_match = match.group(1)
        do_match = match.group(4)
        dont_match = match.group(5)
        
        if mul_match:
            X = int(match.group(2))
            Y = int(match.group(3))
            
            if mul_enabled and 0 < X < 1000 and 0 < Y < 1000:
                product = X * Y
                products.append(product)
        elif do_match:
            mul_enabled = True
        elif dont_match:
            mul_enabled = False
    
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
