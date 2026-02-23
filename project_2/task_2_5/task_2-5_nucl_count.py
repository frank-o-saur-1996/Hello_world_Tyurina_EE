line = "="*3

print (f"{line} Анализ последовательности ДНК {line}\n")
dna = input("Введите последовательность ДНК: ")

dna1 = dna.upper()
lenght = len(dna)

ade = dna1.count("A")
tim = dna1.count("T")
gua = dna1.count("G")
cyt = dna1.count("C")

ade_p = ade / lenght * 100
tim_p = tim / lenght * 100
gua_p = gua / lenght * 100
cyt_p = cyt / lenght * 100

print (f"\nПоследовательность в верхнем регистре: {dna1}\n\nПодсчёт нуклеотидов:\nA: {ade}\nT: {tim}\nG: {gua}")
print(f"C: {cyt}\n\nОбщая длина: {lenght} нуклеотидов\n")
print(f"Процентное содержание каждого нуклеотида:\nA: {ade_p:.2f}%\nT: {tim_p:.2f}%\nG: {gua_p:.2f}%\nC: {cyt_p:.2f}%")