str_text = "Конкатенація (об'єднання) Python — операція склеювання об'єктів " \
           "лінійної структури, зазвичай рядків. Наприклад, конкатенація " \
           "слів «мікро» і «світ» дасть слово «мікросвіт». А, якщо обробити " \
           "необхідно курси валют за останні два роки? Тут нам на допомогу приходять списки. " \
           "Їх можна розглядати як аналог масиву в інших мовах програмування, за винятком важливої " \
           "особливості – списки в якості своїх елементів можуть містити будь-які об'єкти. " \
           "Але про все по порядку. Список (list) в Python є об'єктом (В Python все є об'єктами!!!), " \
           "тому його може бути присвоєно змінній (змінна, як і в попередніх випадках, " \
           "зберігає адресу об'єкта класу «список» Python )." \

list_text = list(str_text.split(" ")) #переводим строку в список, роздільником виступає пробіл
set_text = set(list_text) #переводимо ліст в сет
# print(set_text)
dict_text = {}

counter = 1

for povtor in list_text:
    if povtor == list_text[]

for key_el in set_text:
    dict_text[key_el] = key_el


print(dict_text)

    # counter += 1
    # dict_text[value] = counter


# for key_el in set_text:
#     if key_el ==
#     dict_text[key_el] = key_el




# print(list_text)
# print(set_text)
# print(len(list_text))
# print(len(set_text))




'''a = [1,2,3,4, 'sad']
print(type(a))
b = list(('a','b', 'c'))
print(b)
zm = 'bsad' in a
print(zm)
b = a[2:]
print(b)'''