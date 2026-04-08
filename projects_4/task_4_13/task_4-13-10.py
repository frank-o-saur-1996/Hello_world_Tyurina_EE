a = list(map(int, input('Введите числа через пробел:').split()))
i = 0
sum = 0
n = len(a)
while i < n:
    if i%2 != 0:
        sum = sum + a[i]
    i = i + 1
print(sum)