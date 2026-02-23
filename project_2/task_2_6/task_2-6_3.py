donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()

if donor == recipient or donor == "I":
    print("Переливание крови реципиенту возможно")
elif donor != "I" and donor != recipient:
    print("Переливание крови рецепиенту невозможно")
else:
    print("Ошибка ввода")