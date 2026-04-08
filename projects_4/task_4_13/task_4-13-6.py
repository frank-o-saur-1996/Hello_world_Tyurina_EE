N = int(input())
sum = 0
while N > 0:
    sum = N**2 + sum
    N = N - 1
print(sum)