operator_name = input('Введите имя оператора: ')
number_pres = input('Введите значение датчика давления(Па): ')

with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
        sensor.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n{operator_name}\t{number_pres}")

print('Данные успешно сохранены в sensor_log.txt')