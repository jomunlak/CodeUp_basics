
n = int(input())
# 일의자리수 혹은 10의 자리수에 3, 6, 9가 있으면 짝.
for i in range(1,n+1):
  if i%10 == 3 or i%10 == 6 or i%10 == 9 or i//10 == 3:
    print("X", end = " ")
  else:
    print(i, end = " ") 