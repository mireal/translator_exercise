from words import li
from translator import translate
from random import choice


streak = 0
guess_counter = 0
guess_list = list(range(0, len(li) + 1))
while True:
    guess_num = choice(guess_list)
    guess = li[guess_num]
    guess_list.remove(guess_num)
    counter = 0

    while True:
        print(guess)
        answer = input(f"Переведите слово {guess} на русский: ")
        if not answer:
            quit()
        if answer == translate(guess, "ru", "auto").lower():
            guess_counter += 1
            streak += 1
            print(f'Верно. Правильных ответов: {guess_counter}, подряд: {streak} ')
            break
        else:
            print('Не верно')
            counter += 1
            if counter == 3:
                print(f'Правильный ответ: {translate(guess, "ru", "auto")}')
                counter = 0
                streak = 0
                break
    if not guess_list:
        print('It\'s over')
        quit()
