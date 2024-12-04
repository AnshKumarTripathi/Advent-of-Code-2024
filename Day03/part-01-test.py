import re

def extract_and_validate_instructions(memory):
    products = []
    # Use a regular expression to find all occurrences of mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(memory)
    
    for match in matches:
        X = int(match[0])
        Y = int(match[1])
        
        # Ensure X and Y are valid 1-3 digit numbers
        if 0 < X < 1000 and 0 < Y < 1000:
            product = X * Y
            products.append(product)
    
    return products

def main():
    # Sample corrupted memory string
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    
    # Extract and validate mul(X,Y) instructions
    products = extract_and_validate_instructions(memory)
    
    # Sum the results of all valid mul(X,Y) instructions
    total_sum = sum(products)
    
    # Print the final result
    print("Total sum of valid multiplications:", total_sum)

# Run the main function to execute the program
main()
