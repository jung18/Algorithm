import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

level, nickname = input().split()
rooms.append([(int(level), nickname)])

for _ in range(p-1):
    level, nickname = input().split()
    level = int(level)

    for room in rooms:
        if  len(room) < m and room[0][0] - 10 <= level <= room[0][0] + 10: # 방에 참가
            room.append((level, nickname))
            break
    else:
        rooms.append([(level, nickname)]) # 새 방 생성

for room in rooms:
    room.sort(key=lambda x: x[1])
    
    if len(room) >= m:
        print('Started!')
    else:
        print('Waiting!')

    for lv, name in room:
        print(f'{lv} {name}')