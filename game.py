import random


class User:
    reputation = 50
    quality = 0
    time = 100
    budget = 100

    def __str__(self):
        return 'Rep: ' + str(self.reputation) + ' Quality: ' + str(self.quality) + ' Time: ' + str(
            self.time) + ' Budget: ' + str(self.budget)

    def calculate_points(self, quality, budget, reputation, time):
        self.reputation += reputation
        self.quality += quality
        self.time += time
        self.budget += budget


class Question:

    def __init__(self, answers, text):
        self.answers = answers
        self.text = text

    def print_answers(self):
        for i in range(len(self.answers)):
            print('{0} - {1}'.format(i + 1, self.answers[i]))


def generate_luck(user_reputation):
    random_digit = random.randint(0, 100)

    return random_digit <= user_reputation


q1 = Question(
    [
        'Начну распределять задачи между сотрудниками и постепенно создавать продукт',
        'Оставлю все на последний месяц, а пока дам сотрудникам отдохнуть',
    ],
    'Вы только получили проект и 3 месяца на его выполнение',
)

q2 = Question(
    [
        'Убедить его в том, что изменения не нужны',
        'Согласиться и начать вносить правки',
        'Начать проект заново',
    ],
    'Спустя месяц пришел заказчик первого проекта и потребовал полностью изменить то-то сё-то',
)

q3 = Question(
    [
        'Попросить еще',
        'Уволить часть команды',
        'Найти новые проекты',
    ],
    'У вас заканчиваются деньги',
)

q4 = Question(
    [
        'Отправлю все силы на выполнение нового проекта',
        'Отправлю часть команды',
        'Откажусь от нового проекта',
    ],
    'Внезапно прилетает 2ой проект. Предыдущий - важный для репутации команды, а новый принесет много деняжек. '
    'Как теперь распределить человеческие ресурсы?',
)

q5 = Question(
    [
        'Пусть решают сами',
        'Найму новую команду',
        'Попытаюсь решить конфликт сам',
    ],
    'Произошел конфликт в команде, что будете делать',
)

user = User()

print(q1.text)
print(q1.print_answers())
ans = int(input())
lucky_flag = generate_luck(user.reputation)
if ans == 1:
    user.calculate_points(
        70 if lucky_flag else 30,
        -50 if lucky_flag else -80,
        0,
        -30 if lucky_flag else -50,
    )
elif ans == 2:
    user.calculate_points(
        50 if lucky_flag else 30,
        -80,
        -20,
        -60 if lucky_flag else -120,
    )

print(q2.text)
print(q2.print_answers())
ans = int(input())
lucky_flag = generate_luck(user.reputation)

if ans == 1:
    user.calculate_points(
        40 if lucky_flag else -20,
        0,
        -10,
        0,
    )
elif ans == 2:
    user.calculate_points(
        40 if lucky_flag else -10,
        0,
        10,
        -10,
    )
elif ans == 3:
    user.calculate_points(
        -30 if lucky_flag else -70,
        -50,
        0,
        -30 if lucky_flag else -50,
    )

print(q3.text)
print(q3.print_answers())
ans = int(input())
lucky_flag = generate_luck(user.reputation)

if ans == 1:
    user.calculate_points(
        30 if lucky_flag else 0,
        30 if lucky_flag else 0,
        0 if lucky_flag else -10,
        0,
    )
elif ans == 2:
    user.calculate_points(
        -10,
        0,
        -10,
        -10,
    )
elif ans == 3:
    user.calculate_points(
        -5 if lucky_flag else -10,
        30,
        0,
        -5 if lucky_flag else -10,
    )

if ans == 3:

    print(q4.text)
    print(q4.print_answers())
    ans = int(input())
    lucky_flag = generate_luck(user.reputation)

    if ans == 1:
        user.calculate_points(
            -20 if lucky_flag else -70,
            100,
            -10,
            40,
        )
    elif ans == 2:
        user.calculate_points(
            -20 if lucky_flag else -40,
            70,
            5,
            -20,
        )
    elif ans == 3:
        user.calculate_points(
            30 if lucky_flag else 0,
            0,
            0,
            40,
        )

print(q5.text)
print(q5.print_answers())
ans = int(input())
lucky_flag = generate_luck(user.reputation)

if ans == 1:
    user.calculate_points(
        0 if lucky_flag else -20,
        0 if lucky_flag else -20,
        0 if lucky_flag else -10,
        0 if lucky_flag else -15,
    )
elif ans == 2:
    user.calculate_points(
        10 if lucky_flag else -10,
        0 if lucky_flag else -10,
        0,
        10 if lucky_flag else -10,
    )
elif ans == 3:
    user.calculate_points(
        10 if lucky_flag else -10,
        0,
        10 if lucky_flag else -10,
        10 if lucky_flag else -10,
    )

print(user)

if user.quality >= 75 and user.time > 0 and user.reputation > 0 and user.budget > 0:
    print('YOU W0N THIS GAME!!!')
else:
    print('YOU LOSE THIS GAME!!!')
