def file_processing(text: str, filename: str):
    with open(filename, 'a+', encoding='utf-8') as f:
        f.seek(0)
        content = f.read()
        f.write(text if len(content) == 0 else f'\n{text}')
        f.seek(0)
        lines = [line.rstrip('\n') for line in f]

    print("Содержимое всех четных строк:")
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            print(line)

usertext = input("текст в файл: ")
userfile = input("имя файла: ")
file_processing(usertext, userfile)