# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc',
# то заменить их на 'www', иначе добавить в конец строки 'zzz'.

text = input('Enter text >: ')

end_str = 'zzz'

if text.startswith('abc'):
    print(text.replace('abc', 'www'))
else:
    text += end_str
    print(text)
