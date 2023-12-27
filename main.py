import string
import random


import string
import random


def input_text():
    return


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
            pass
        elif point == "2":
            pass
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
            pass
        elif point == "4":
            print("Программа завершена")
            break
            pass
        else:
            print("Выберите верный пункт меню")
            pass


if __name__ == 'main':
    main()