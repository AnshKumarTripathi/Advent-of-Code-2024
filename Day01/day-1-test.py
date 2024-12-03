listA = [3,4,2,1,3,3]
listB = [4,3,5,3,9,3]

listA.sort()
listB.sort()

totalDis = 0

n = len(listA)

for i in range(n):
  d = listA[i] - listB[i]
  if(d < 0):
    d = -d
  else:
    pass
  
  totalDis = d + totalDis
  
print(totalDis)