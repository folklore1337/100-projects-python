import time
import random

word_list = ["рубик", "магнус", "антимаг", "некрофос", "темпларка"]

word = random.choice(word_list)

name = input("Вы готовы играть? У вас 10 попыток! ")

print("Привет! Время играть в виселицу-Дота!")

time.sleep(1)

print("Генерируем слово...")
time.sleep(0.5)

guesses = ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    if failed == 0:
        print("\nВы победили!")
        break

    guess = input("\nУгадайте героя из доты: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Неверно")
        print("У вас осталось", turns)
        if turns == 0:
            print("\nТы проиграл!")
