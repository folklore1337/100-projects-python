import random

# Словарь с данными о государствах и их столицах
capitals = {
    'Швеция': 'Стокгольм',
    'Италия': 'Рим',
    'Франция': 'Париж'
}

# Получаем случайный порядок вопросов
questions = list(capitals.keys())
random.shuffle(questions)

# Проходимся по каждому вопросу в случайном порядке
for country in questions:
    capital = capitals[country]
    answer = input(f'Столица какого государства является город {capital}?: ')
    
    # Проверяем правильность ответа пользователя
    if answer == country:
        print('Правильно, идем дальше!')
    else:
        print('Неправильно, попробуйте еще раз!')
        break
else:
    print('Поздравляем, вы ответили правильно на все вопросы!')
