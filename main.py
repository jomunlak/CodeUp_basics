

n = int(input()) # 출석번호 부를 횟수
chulseok = list(map(int,input().split()))
numList = [0] * 23


for i in range(n):
  numList[chulseok[i]-1] += 1

for i in numList:
  print(i, end =" ")
