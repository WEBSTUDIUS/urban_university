# ункты задачи:
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not message:
        print('Nothing to send. Add message')
        return False
    if not check_email(recipient) or not check_email(sender):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        return False
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return False
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')

    return True


def check_email(email):
    if '@' not in email:
        return False
    if email[-4:] != '.com' and email[-3:] != '.ru' and email[-4:] != '.net':
        return False

    return True


send_email('message', 'asd@asd.com', sender='asd@as.com')
