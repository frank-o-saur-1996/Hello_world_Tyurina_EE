weight = int(input("Введите ваш вес (кг): "))
height = int(input("Введите ваш рост (см): "))
line = "-" * 3
height1 = height / 100
bmi = weight / (height1 ** 2)

print(f"{line} Отчет о состоянии здоровья {line}\nРост:\t{height} см\nВес:\t{weight} кг\nИндекс массы тела: {bmi:.2f}")