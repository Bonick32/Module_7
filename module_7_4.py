team_1 = 'Мастера кода'
team_2 = 'Волшебники Данных'
team1_num = 5
team2_num = 6
score_2 = 42
team1_time = 10717.6
team2_time = 18015.2
score_1 = 40
tasks_total = score_1 + score_2
time_avg = round(((team1_time + team2_time) / tasks_total), 1)

print("В команде Мастера кода участников: %(team1_num)s!" % {'team1_num' : '5'})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num' : '5', 'team2_num' : '6'})

print("Команда Волшебники данных решила задач: {score_2}!".format(score_2=42))
print("Волшебники данных решили задачи за {team2_time}с!".format(team2_time=18015.2))

print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {team_1}'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {team_2}'
else:
    result = 'Ничья!'

challenge_result = result
print(challenge_result)

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')




