# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birth_date, city, email, phone):
    return f"Name: {name}\n" \
           f'Surname: {surname}\n' \
           f"Birth date: {birth_date}\n" \
           f"City: {city}\n" \
           f"Email: {email}\n" \
           f"Phone number: {phone}"

print(user_info(name="Andrey",
                surname='Krylov',
                birth_date='14.11.1988',
                city='Moscow',
                email="ak.chemp@gmail.com",
                phone='+79779264986'))