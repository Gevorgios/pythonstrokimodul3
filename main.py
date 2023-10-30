#
# string = input("Введите строку: ")
#
#
# reversed_string = string[::-1]
#
#
# print("Результат поворота строки:", reversed_string)



#
# string = input("Введите строку: ")
#
#
# letter_count = 0
# digit_count = 0
#
#
# for char in string:
#
#     if char.isalpha():
#         letter_count += 1
#
#     elif char.isdigit():
#         digit_count += 1
#
#
# print("Количество букв в строке:", letter_count)
# print("Количество цифр в строке:", digit_count)



# string = input("Введите строку: ")
#
#
# character = input("Введите символ для поиска: ")
#
#
# count = 0
#
#
# for char in string:
#     if char == character:
#         count += 1
#
#
# print("Символ", character, "встречается", count, "раз(а) в строке.")

# string = input("Введите строку: ")
# word = input("Введите слово для поиска: ")
#
#
# count = 0
#
#
# for char in string:
#     if char == word:
#         count += 1
#
#
# print("Слово", word, "встречается", count, "раз(а) в строке.")


# string = input("Введите строку: ")
#
#
# word = input("Введите слово для поиска: ")
#
#
# words_list = string.split()
#
#
# count = 0
#
#
# for w in words_list:
#
#     if w == word:
#         count += 1
#
#
# print("Слово", word, "встречается", count, "раз(а) в строке.")


# string = input("Введите строку: ")
#
#
# word_to_find = input("Введите слово для поиска: ")
#
#
# word_to_replace = input("Введите слово для замены: ")
#
#
# new_string = string.replace(word_to_find, word_to_replace)
#
#
# print("Полученная строка:", new_string)