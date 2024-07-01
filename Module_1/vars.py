# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

home_tasks_done = 12
hours_taken = 1.5
course_name = 'Python'
time_for_task = hours_taken / home_tasks_done
print(
    'Course: ' + course_name +
    ', total tasks: ' + str(home_tasks_done) +
    ', hours taken: ' + str(hours_taken) +
    ', average time per task: ' +
    str(time_for_task) + ' hours'
)
print(
    'Course:', course_name,
    ', total tasks:', home_tasks_done,
    ', hours taken:', hours_taken,
    ', average time per task:',
    str(time_for_task), ' hours'
)
