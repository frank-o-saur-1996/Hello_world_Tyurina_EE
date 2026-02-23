volume = float(input('Введите нужный объем раствора(мл): '))
mass = volume * 0.009
line = "-"*23

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n{line}\nОбщий объем: {volume} мл\nМасса соли:  {mass:.2f} г\nОбъем воды:  {volume} мл")