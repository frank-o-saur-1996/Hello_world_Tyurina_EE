protein = int(input('Введите массу белков в продукте(г): '))
fats = int(input('Введите массу жиров в продукте(г): '))
carbons = int(input('Введите массу углеводов в продукте(г): '))

total = (protein * 4)+(fats * 9)+(carbons * 4)

print(f"Общая калорийность: {total} ккал")