file_name = input("Введите имя файла: ")

with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    i = 0
    for lines[i] in lines:
        print(f'{i + 1} {lines[i].rstrip()}')
file.close()