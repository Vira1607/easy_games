import random


def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    target = random.randint(1, 3)
    proba = int(input('Выберите: камень, ножницы или бумага?\n1 — камень\n2 — ножницы\n3 — бумага\n'))
    if target == proba:
      print('Победила дружба!')
    elif (proba - target == 1) or (proba - target == -2):
      print('Поздравляем! Вы выиграли!')
    else:
      print('Упс, поражение')
    again = input('Ещё раз? (1 — да, 0 — нет))')
    return again


def guess_the_number():
    #Здесь будет игра "Угадай число"
    target = random.randint(0, 9)
    proba = int(input('Введите число от 0 до 9: \n'))
    while proba != target:
        proba = int(input('Пока не угадали, попробуйте ещё раз! :) \n'))
    print('Поздравляем! Вы выиграли!')
    again = input('Ещё раз? (1 — да, 0 — нет))')
    return again


def mainMenu():
    #Здесь главное меню игры
    swing = int(
        input(
            'Во что будем играть? \n1 — "Камень, ножницы, бумага" \n2 — "Угадай число" \n'
        ))
    if (swing == 1):
        new_game_1 = rock_paper_scissors()
    else:
        new_game_2 = guess_the_number()
    if (new_game_1 == 0) and (new_game_2 == 0):
      again = input('Поиграем снова? (1 — да, 0 — нет))')
      return again

new_game_1 = 0
new_game_2 = 0

again = mainMenu()

while new_game_1 == '1':
  rock_paper_scissors()

while new_game_2 == '1':
  guess_the_number()

while again == '1':
  again = mainMenu()
