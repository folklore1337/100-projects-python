alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

total = int(input('Количество сдвигов для шифрования: '))
message = input("Сообщение для шифрования: ").upper()
ready = ''

for i in message:
    if i in alphabet:
        m = alphabet.find(i)
        new_mesto = m + total 
        ready += alphabet[new_mesto]
    else:
        ready += i
print(ready.lower())
