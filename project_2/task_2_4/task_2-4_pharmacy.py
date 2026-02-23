pills_amount = int(input('Введите количество произведенных капсул: '))
pack_capacity = int(input('Введите вместимость одной упаковки: '))
line = "-" * 3

full_packs = pills_amount // pack_capacity
pills_left = pills_amount % pack_capacity
89
print(f"{line} Отчет фасовочного цеха {line}\nПолных упаковок:\t{full_packs}\nОстаток капсул:\t{pills_left}")