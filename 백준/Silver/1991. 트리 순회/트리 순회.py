N = int(input())

tree = {}
pre_ans = ''
in_ans = ''
post_ans = ''

def pre_order(node):
    global pre_ans
    pre_ans += node
    if tree[node][0] != '.':
        pre_order(tree[node][0])
    if tree[node][1] != '.':
        pre_order(tree[node][1])

def in_order(node):
    global in_ans
    if tree[node][0] != '.':
        in_order(tree[node][0])
    in_ans += node
    if tree[node][1] != '.':
        in_order(tree[node][1])
        
def post_order(node):
    global post_ans
    if tree[node][0] != '.':
        post_order(tree[node][0])
    if tree[node][1] != '.':
        post_order(tree[node][1])
    post_ans += node
        
# 트리 연결하기
for _ in range(N):
    p, l, r = input().split()
    tree[p] = [l, r]

pre_order('A')
in_order('A')
post_order('A')

print(pre_ans)
print(in_ans)
print(post_ans)