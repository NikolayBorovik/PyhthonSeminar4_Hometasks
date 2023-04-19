# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

n = int(input('Enter size of the 1st set: '))
m = int(input('Enter size of the 2nd set: '))

list1 = [randint(0,9) for i in range(n)]
print(list1)
list1 = set(list(list1))
print(list1)


list2 = [randint(0,9) for i in range(m)]
print(list2)
list2 = set(list(list2))
print(list2)

gen_list = list(list1.intersection(list2))
print(gen_list)

for i in range (len(gen_list)-1):
    if gen_list[i] > gen_list[i+1]:
        temp = gen_list[i]
        gen_list[i] = gen_list[i+1]
        gen_list[i+1] = temp


print(gen_list)
