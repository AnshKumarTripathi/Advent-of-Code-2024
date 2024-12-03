def read_lists_from_file(filename):
    listA = []
    listB = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            left, right = map(int, line.split())
            listA.append(left)
            listB.append(right)
    return listA, listB

def calculate_similarity_score(listA, listB):
    score = 0
    for i in listA:
        count = 0
        for j in listB:
            if i == j:
                count += 1
        score += i * count
    return score

# Read lists from the text file
listA, listB = read_lists_from_file('input.txt')

# Calculate the similarity score
similarity_score = calculate_similarity_score(listA, listB)
print("Similarity Score:", similarity_score)
