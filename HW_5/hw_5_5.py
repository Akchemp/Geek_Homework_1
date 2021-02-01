"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
with open("task_4.txt", "w") as f:
    num = f"{input('Введите числа через пробел: ')}"
    f.write(num)
with open("task_4.txt", "r") as f:
    main_line = f.readline()
    main_list = map(int, main_line.split())
    print(sum(main_list))