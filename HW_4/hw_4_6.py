"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle

print("The program generates integers starting from the specified one. To generate a number"
      "You must press Enter. For exit - q")
for i in count(int(input('Enter start number: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print("The program repeats the elements of the list. To generate the next repetition"
      "press Enter, to exit - enter q.")
u_list = input("enter a list, separating the items with a space: ").split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()