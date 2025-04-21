import sys
input = sys.stdin.readline


def collections(i, start):
    if i == 6:
        for num in path:
            print(num, end=" ")
        print()
        return
    
    for j in range(start, k):
        path.append(S[j])
        collections(i+1, j+1)
        path.pop()


board = []
path = []

while True:
    line = list(map(int, input().strip().split()))
    
    if line[0] == 0:
        break
    
    board.append(line)

for line in board:
    S = line[1:]
    k = line[0]
    
    collections(0, 0)
    print()