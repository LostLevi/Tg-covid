def start_msg(message, world):
    start_msg = f'''<b>Привет {message}</b>\nПо всему миру кол-во зараженных уже достигло <b>{world}</b> человек.\nЭтот бот создан для удобного ознакомления со статистикой\nЧто умеет бот:\n1. Для обновления статистики по России нажмите на кнопку "Обновить данные"\n2. Для того, что бы узнать статистику определенного города, введите его название (например: <b>Москва</b>)\n<i>Не болейте и не скучайте (с) LostLevi</i>'''
    return(start_msg)

def full_msg(illed, day_stat_ill, day_res, deaths, illed_procent):
    full_msg = f"Всего заражено в России: <b>{illed}</b>\nЗа последние сутки заразилось: <b>{day_stat_ill}</b>\nВыздоровевших: <b>{day_res}</b>\nПогибших: <b>{deaths}</b>\n<i>Заражено: <b>{illed_procent}%</b> населения</i>"
    return(full_msg)

def city_msg():
    city_msg = f"Фыр"
    return(sity_msg)
