import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().split()))
points_set = list(set(points))
points_set.sort()

point_dict = {}

for i in range(len(points_set)):
    point_dict[points_set[i]] = i

for p in points:
    print(point_dict[p], end=' ')