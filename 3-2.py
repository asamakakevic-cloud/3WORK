def s(a,b): return a+b
def v(a,b): return a-b
def u(a,b): return a*b
def d(a,b):
    if b==0: raise ZeroDivisionError("На ноль нельзя!")
    return a/b
def st(a,b): return a**b
def f(n):
    if n<0: raise ValueError("Отрицательное!")
    r=1
    for i in range(2,n+1): r*=i
    return r
def k(n):
    if n<0: raise ValueError("Отрицательное!")
    if n==0: return 0
    x=n/2
    for _ in range(20): x=(x+n/x)/2
    return x
def sr(s):
    ch=[float(x) for x in s.split()]
    return sum(ch)/len(ch)

ops={"1":s,"2":v,"3":u,"4":d,"5":st,"6":f,"7":k,"8":sr}
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Факториал")
print("7. Синус")
print("8. Медиана")
while True:
    print("-"*20)
    w=input("Операция: ")
    if w=="exit": break
    try:
        if w in "12345":
            a=float(input("a: ")); b=float(input("b: "))
            print(">>>",ops[w](a,b))
        elif w=="6":
            n=int(input("n: ")); print(">>>",f(n))
        elif w=="7":
            n=float(input("n: ")); print(">>>",k(n))
        elif w=="8":
            print(">>>",sr(input("Числа: ")))
    except Exception as e: print("Ошибка:",e)