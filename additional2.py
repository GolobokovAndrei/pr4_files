file_name = input("Введите имя файла: ")
n = int(input("Введите количество последних строк для вывода: "))

with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.rstrip())