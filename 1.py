file_name = input("Введите имя файла: ")
print('Начните вводить строки:')

inputs = []

current_input = ''

while True:
    current_input = input()
    if current_input == '':
        break
    inputs.append(current_input)

with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
    i = 0
    for inputs[i] in inputs:
        if i == len(inputs) - 1:
            file.write(inputs[i])
            break
        file.write(inputs[i] + '\n')
        i += 1
file.close()