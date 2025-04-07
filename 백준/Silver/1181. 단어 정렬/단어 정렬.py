import sys
input = sys.stdin.readline

words = set() # 중복제거
for _ in range(int(input())):
    words.add(input().strip('\n'))

words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)