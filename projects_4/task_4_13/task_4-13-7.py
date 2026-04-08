a = list(map(int, input('Введите числа через пробел:').split()))
n = len(a)
sum = 0
i = 0
while i < n:
  sum = sum + a[i]
  i = i + 1
print(sum/n)  