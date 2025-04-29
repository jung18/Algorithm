import sys
input = sys.stdin.readline


def cal(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    else:
        if num1 < 0 and num2 > 0:
            return -(-num1 // num2)
        return num1 // num2


def permutation(i, tmp):
    if i == N-1:
        answer.append(tmp)
        return
    
    for j in range(0, N-1):
        if not visited[j]:
            visited[j] = 1
            permutation(i+1, cal(tmp, An[i+1], operator_str[j]))
            visited[j] = 0


N = int(input())
An = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_str = ['+'] * operator[0] + ['-'] * operator[1] + ['*'] * operator[2] + ['/'] * operator[3]

visited = [0 for _ in range(N-1)]
answer = []

permutation(0, An[0])
answer.sort()

print(answer[-1])
print(answer[0])