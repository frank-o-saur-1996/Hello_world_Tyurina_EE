substrat_name = input('Введите название питательной среды: ')
agar_conc = input('Введите концентрацию агара(%): ')
sterilization_temp = input('Введите температуру стерилизации: ')

with open("recipe.txt", "w", encoding="utf-8") as recipe:
        recipe.write(f"\t{substrat_name}\nКонцентрация агара(%): {agar_conc}\nТемпература стерилизации: {sterilization_temp}")

print("Файл 'recipe.txt' успешно сформирован!")