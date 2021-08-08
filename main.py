
n = int(input())

myList = [300,60,10]
countList = [0,0,0]


for i in range(3):
  countList[i]= n // myList[i]

  n = n % myList[i] 

if n != 0 :
  print("-1")
else:
  for i in range(3):
    print(countList[i], end = " ")