a = list(map(int, input('Введите числа через пробел:').split()))
i = 0
sum = 0
n = len(a)
while i < n:
    if a[i] > 0:
        sum = sum + 1
    i = i + 1
print(sum)