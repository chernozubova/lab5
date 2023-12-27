import string
import random


def input_text():
    input_type = input(
        "Выберите тип ввода данных: \n1. вручную\n2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        text = input("Введите текст: ")
    elif input_type == '2':
        n = int(input("Введите длину генерируемого текста: "))
        text = ''.join(random.choice(string.ascii_letters + string.punctuation + " ") for _ in range(n))
    else:
        print("Неверный тип ввода данных")
        text = None
    return text


def count(text):
    cnt_lowercase = 0
    cnt_uppercase = 0
    cnt_punctuation = 0
    cnt_whitespace = 0

    for char in text:
        if char.islower():
            cnt_lowercase += 1
        elif char.isupper():
            cnt_uppercase += 1
        elif char in ['.', ',', '!', '?', ':', ';']:
            cnt_punctuation += 1
        elif char.isspace():
            cnt_whitespace += 1

    return cnt_lowercase, cnt_uppercase, cnt_punctuation, cnt_whitespace


def main():
    while True:
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Решение задания")
        print("3. Результат работы алгоритма")
        print("4. Завершение работы программы")

        point = input("Введите пункт меню: ")

        if point == "1":
            text = input_text()
        elif point == "2":
            if 'text' in locals():
                result = count(text)
                print("Исходные данные: ", text)
                print("Задание решено")
            else:
                print("Исходные данные не введены")
        elif point == "3":
            if 'result' in locals():
                cnt_lowercase, cnt_uppercase, cnt_punctuation, cnt_whitespace = result
                print("Результат:")
                print("Количество строчных букв:", cnt_lowercase)
                print("Количество прописных букв:", cnt_uppercase)
                print("Количество знаков препинания:", cnt_punctuation)
                print("Количество пробелов:", cnt_whitespace)
            else:
                print("Входные данные не сгенерированы")
        elif point == "4":
            print("Программа завершена")
            break
        else:
            print("Выберите верный пункт меню")


if __name__ == '__main__':
    main()
