# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc',
# то заменить их на 'www', иначе добавить в конец строки 'zzz'.

enter_text = input('Enter text >: ')
end_str = 'zzz'

if enter_text.startswith('abc'):
    print(enter_text.replace('abc', 'www'))
else:
    enter_text += end_str
    print(enter_text)
