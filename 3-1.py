def multiply_elements(spisok, mnozhitel=2):
    noviy_spisok = []
    for element in spisok:
        noviy_spisok.append(element * mnozhitel)
    return noviy_spisok

vvod = input("Введите список чисел через пробел: ")
chisla = vvod.split()

obrabotanniy_spisok = []
for slovo in chisla:

    if slovo.isdigit() or (slovo[0] == '-' and slovo[1:].isdigit()):
        obrabotanniy_spisok.append(int(slovo))
    else:
        obrabotanniy_spisok.append(slovo)


m = input("Введите множитель (по умолчанию 2): ")
if m == "":
    mnozhitel = 2
else:
    mnozhitel = int(m)


rezultat_funkcii = multiply_elements(obrabotanniy_spisok, mnozhitel)
print("Результат (функция):", rezultat_funkcii)


lambda_rezultat = list(map(lambda x: x * mnozhitel, obrabotanniy_spisok))
print("Результат (лямбда-функция):", lambda_rezultat)