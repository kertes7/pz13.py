#task 1

filename = input("Введіть назву файлу: ")

with open(filename, 'w', encoding='utf-8') as file:
    print("Введіть текст (порожній рядок для завершення):")
    while True:
        line = input()
        if line == "":
            break
        file.write(line + '\n')

with open(filename, 'r', encoding='utf-8') as file:
    print("\nВміст файлу:")
    print(file.read())


#task 2

filename = input("Введіть назву файлу для аналізу: ")

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
    lines = text.split('\n')
    words = text.split()
    chars = len(text)

print(f"Кількість рядків: {len(lines)}")
print(f"Кількість слів: {len(words)}")
print(f"Кількість символів: {chars}")


#task 3

filename = input("Введіть назву файлу для редагування: ")
word_to_find = input("Що шукаємо: ")
replacement = input("На що замінити: ")

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

new_content = content.replace(word_to_find, replacement)

new_filename = "new_" + filename
with open(new_filename, 'w', encoding='utf-8') as file:
    file.write(new_content)

print(f"Збережено у файл: {new_filename}")

