#  Создайте собственный класс-исключение, который должен проверять
#  содержимое списка на наличие только чисел. Проверить работу
#  исключения на реальном примере. Необходимо запрашивать у пользователя
#  данные и заполнять список только числами. Класс-исключение должен
#  контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный список с числами
# выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':

    numbers = []
    while True:
        inp_data = input("Введите число: ")
        print(f'Вы ввели: {inp_data}')

        try:
            if inp_data.isdigit():
                numbers.append(int(inp_data))
            elif inp_data == "stop":
                print("Game over!")
                print(f'Ваши числа: {numbers}')
                exit(0)
            else:
                raise MyError(f"Вы ввели {inp_data}")
        except MyError as err:
            print(f'Ошибка: {err}')