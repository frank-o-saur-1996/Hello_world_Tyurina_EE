line = "-"*43
researcher_name = input('Введите имя исследователя: ')
data = input('Введите дату: ')
experiment = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')

with open("journal.txt", "w", encoding="utf-8") as journal:
    journal.write(f"+{line}+\n|Электронный лабораторный журнал\t\t\t|\n+{line}+\n|ФИО исследователя: {researcher_name} |\n|Дата\t\t\t\t: ")
    journal.write(f"{data}\t\t\t|\n|Эксперимент\t\t: {experiment}\t\t|\n+{line}+\n|Вывод:\t\t\t\t\t\t\t\t\t\t|\n|{conclusion}|\n+{line}+")