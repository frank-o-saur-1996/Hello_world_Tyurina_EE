l = list(map(int, input('Введите числа через пробел:').split()))
max = 0
n = len(l)
c = 0
while c < n:
  if l[c] > max:
    max = l[c]
    c = c + 1
print(max) 