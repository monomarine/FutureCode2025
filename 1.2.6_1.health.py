# 0-30 - без сознания 31 - 70 - ранен 71-90 - легкое недомогаение 91 - здоров

health = int(input("введите уровень здоровья : "))

if health >= 90:
    print('персонаж здоров')

elif 70 <= health < 90:
    print('вам нужно выпить зелье. согласны? (Y / N) ')
    answer = input()
    if answer.lower() == 'y':
        health += 10
        print('здоровье увеличено до ', health)

elif 30 <= health < 70:
    print('вы ранены. использовать аптечку? (Y / N) ')
    answer = input()
    if answer.lower() == 'y':
        health += 30
        print('здоровье увеличено до ', health)

else:
    print('персонаж без сознания')