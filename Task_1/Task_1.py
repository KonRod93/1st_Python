# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите трехзначное число: ")
n = int(input())
s = str(n)
a = int (s[0])
b = int (s[1])
c = int (s[2])
print (a+b+c)

# Вариант для любого числа
# print("Введите число: ")
# n = int(input())
# s = str(n) 
# sum = 0
# for i in range (len(s)):
#     sum+int(s[i])
# print (sum)   