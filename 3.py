file_name = input("Введите имя файла: ")
n = int(input("Введите максимальное число строк: "))

with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

i = 1
while len(lines) > 0:
    lines_to_write = lines[:n]
    
    with open(f'3_output/{i}.txt', 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines_to_write)
    
    lines = lines[n:]
    
    i += 1

file.close()