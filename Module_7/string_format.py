team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 6
print('В команде %(team)s участников: %(num)s' % {'team': team1, 'num': team1_num} + '!')
team2_num = 5
print('Итого сегодня в командах участников: %(team1)s и %(team2)s' % {'team1': team1_num, 'team2': team2_num} + '!')
score_1 = 40
score_2 = 42
print('Команда Волшебники данных решила задач: {score_2}'.format(score_1=score_1, score_2=score_2) + '!')
team1_time = 18015.2
team2_time = 22013.5
print('Волшебники данных решили задачи за {team2_time}'.format(team1_time=team1_time, team2_time=team2_time) + 'с !')
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team2}!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')
task_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / task_total, 1)
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!.')