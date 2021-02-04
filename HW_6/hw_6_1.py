"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный.
 В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
 Продолжительность первого состояния
 (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""


from itertools import cycle
from time import sleep


class TrafficLight:
    __colors = {"Красный": 7, "Желтый": 2, "Зеленый": 7}
    prev_colors = {"Красный": "Зеленый", 'Зеленый': 'Желтый', "Желтый": "Красный"}

    def running(self, run_count):
        colors_iteration = cycle(self.__colors)
        prev_color = "Зеленый"
        while run_count:
            current_light_value = next(colors_iteration)
            if TrafficLight.prev_colors[current_light_value] != prev_color:
                raise ValueError("Наружен порядок!")
            print(f"Сейчас горит сигнал: {current_light_value} "
                  f"{TrafficLight.__colors[current_light_value]} сек."
                  f"(Предыдущий: {prev_color})")
            sleep(self.__colors[current_light_value])
            prev_color = current_light_value
            run_count -= 1

    def get_colors(self, keyword):
        if keyword == "админ пароль":
            return self.__colors
        else:
            ValueError("Ошибка авторизации")


traffic_light = TrafficLight()
traffic_light.running(5)
print(traffic_light.get_colors("админ пароль"))
