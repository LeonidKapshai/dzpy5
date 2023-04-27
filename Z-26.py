# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
a = int (input("Введите число: "))
b = int (input("Введите число: "))

# def Exponent(a,b):
#     sum = 1
#     for i in range (b):
#         sum = sum * a
#         i+=1 
#     return sum

def Exponent(a,b):
    if b<0:
        return 1/a * Exponent(a,b+1)
    if b==0:
        return 1
    return Exponent(a,b-1)*a

print(f'Число {a} в степени {b} - {Exponent(a,b)}')
