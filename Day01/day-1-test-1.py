listA = [3,4,2,1,3,3]
listB = [4,3,5,3,9,3]


score = 0

for i in listA:
  count = 0
  for j in listB:
    if(i == j):
      count = count + 1
  score += i * count

  
print(score)