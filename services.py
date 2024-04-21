import random


def random_seconds(sec):
    """
    Функция получения случайного диапазона времени в секундах
    :param sec: начальное время в секундах
    :return: случайное время в секундах, но не менее начального
    """
    value = random.random()
    time_value = sec + (value * 20)
    return time_value
