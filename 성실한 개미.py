

mapp = []
for _ in range(10):
  mapp.append(list(map(int,input().split()))) # 이차원 리스트 입력받기

ant_x = 1
ant_y = 1 # 개미의 출발지점 설정

while(mapp[ant_y][ant_x]!=2): # 현재 지점이 먹이가 있는 지점이라면 탈출
  mapp[ant_y][ant_x] = 9

  if mapp[ant_y][ant_x+1] == 0 or mapp[ant_y][ant_x+1] == 2: #오른쪽이 비어있다면 오른쪽 먼저 
    ant_x += 1
  elif mapp[ant_y+1][ant_x] == 0 or mapp[ant_y+1][ant_x] == 2: #오른쪽이 막혀있다면 아래쪽으로
    ant_y += 1
  else:
    break  # 갈곳이 없다면 반복문 탈출

mapp[ant_y][ant_x] = 9 # 먹이 먹기


for i in range(10):
  for j in range(10):
    print(mapp[i][j], end=" ")
  
  print()
