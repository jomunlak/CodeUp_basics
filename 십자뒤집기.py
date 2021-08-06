
badukpanList = []
for _ in range(19):
  badukpanList.append(list(map(int,input().split())))


n = int(input()) # 반복할 수

for _ in range(n):
  x, y = map(int,input().split())
  for i in range(19):
    if badukpanList[x-1][i] == 0:
      badukpanList[x-1][i] = 1
    else:
      badukpanList[x-1][i] =0
  for i in range(19):
    if badukpanList[i][y -1] == 0:
      badukpanList[i][y -1] = 1
    else:
      badukpanList[i][y -1] =0


for i in range(19):
  for j in range(19):
    print(badukpanList[i][j], end =" ")
  print()
