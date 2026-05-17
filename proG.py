n = int(input())
current = 0
mx = 0
for _ in range(n):
    a, b = map(int, input().split())
    current -= a
    current += b
    mx = max(mx, current)

print(mx)