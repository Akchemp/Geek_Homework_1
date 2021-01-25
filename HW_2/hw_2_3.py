# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


seasons_list = ['January', 'February', 'March', 'April', 'May', 'June',
                'Jule', 'August', 'September', 'October', 'November', 'December']

seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: "autumn"}

month = int(input('Enter month from 1 to 12: '))

if month == 1:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[1])
elif month == 12:
    print(seasons_dict.get(1))
    print(seasons_list[11])
elif month == 3:
    print(seasons_dict.get(2))
    print(seasons_list[2])
elif month == 4:
    print(seasons_dict.get(2))
    print(seasons_list[3])
elif month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[4])
elif month == 6:
    print(seasons_dict.get(3))
    print(seasons_list[5])
elif month == 7:
    print(seasons_dict.get(3))
    print(seasons_list[6])
elif month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[7])
elif month == 9:
    print(seasons_dict.get(4))
    print(seasons_list[8])
elif month == 10:
    print(seasons_dict.get(4))
    print(seasons_list[9])
elif month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[10])
else:
    print("No such month exists.")