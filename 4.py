input_files = ['3_output/1', '3_output/2', '3_output/3']
output_file = input("Введите имя выходного файла: ")

with open(f'{output_file}.txt', 'w', encoding='utf-8') as outfile:
    for file_name in input_files:
        with open(f'{file_name}.txt', 'r', encoding='utf-8') as infile:
            outfile.write(infile.read() + '\n')