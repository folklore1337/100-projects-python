string = input(str('Enter your word (in lowercase): '))

vowels = ['a', 'e', 'o', 'i', 'u', 'y']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print(result)
