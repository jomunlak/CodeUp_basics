

r,c = map(int,input().split())
myList = [[0 for _ in range(c)] for _ in range(r)]

n = int(input()) # 막대의 개수

for _ in range(n):
  l, d, x, y = map(int,input().split()) # 길이, 방향(0: 가로, 1: 세로), 좌표

  if(d == 0): # 가로? 세로?
    for i in range(l):
      myList[x-1][y-1+i] = 1
  else:
    for i in range(l):
      myList[x-1+i][y-1] = 1



for i in range(r):
  for j in range(c):
    print(myList[i][j], end =" ")
  print()