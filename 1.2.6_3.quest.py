from random import randint

hp = 100
rooms = 10
rooms_content = ['лава', 'пустая комната', 'орк']


while hp > 0 and rooms > 0:
    print('перед вами 3 двери. в какую войдете? (1 / 2 / 3) ')
    answer = int(input())
    rooms -= 1
    if 0 < answer <= 3:
        i = randint(0, len(rooms_content) - 1)
        content = rooms_content[i]
        print('вам открылась комната - ', content)
        if content != 'пустая комната':
            damage = randint(10, 31)
            hp -= damage
            print("вам нанесен урон",damage, "Осталось", hp, "здоровья")

if hp > 0:
    print('Вы прошли весь лабиринт')
else:
    print('вы проиграли')