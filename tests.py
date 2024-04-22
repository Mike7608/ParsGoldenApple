import sys
import unittest
from io import StringIO

import settings
from main import get_one_item
from parsGoldApple import ParsGoldApple


class TestMain(unittest.TestCase):
    def test_get_one_item(self):
        """
        Тест получения оной записи по заданной ссылке и вывода его на экран
        """
        # Подготовка данных для теста
        url = "https://goldapple.ru/19000201893-raffaello"

        # Перенаправление стандартного вывода в буфер
        captured_output = StringIO()
        sys.stdout = captured_output

        # Вызов тестируемой функции
        get_one_item(url)

        # Восстановление стандартного вывода
        sys.stdout = sys.__stdout__

        # Получение вывода функции
        output = captured_output.getvalue().strip()

        # Проверка содержания вывода

        self.assertEqual(output, str("{'id': '19000201893', 'url': 'https://goldapple.ru/19000201893-raffaello', 'name': 'PANTHEON ROMA RAFFAELLO', 'price': '27300', 'currency': 'RUB', 'rate': '5.0', 'description': 'Он очень утонченный и эклектичный гений, в то же время сильный и конкретный. Профиль художника, сделавшего элегантность отличительной чертой своей работы. Изящество его штриха оставило неизгладимый след в истории искусства. Рафаэль —привлекательный, элегантный и страстный мужчина, полностью проживший свою историю любви. Обработка аромата проходит на двух уровнях: дистиллят чистого большого абсента и смесь перца, кожи, тикового дерева и бобов тонка. На первом уровне художник и его вибрация (абсент), на втором рассказывается вместо энергии (кожа, перец, тик и бобы тонка), с фоновым запахом, напоминающим цветные пигмент', 'instruction': 'Наносить на неповрежденные участки кожи, волос и одежду', 'made': 'страна происхождения: Италия; изготовитель:JOY S.P.A Via, del Lavoro 13, 61045, Pergola, Italy;'}"))
        # Замените "Ожидаемый вывод функции" на ожидаемый текст, который должен быть выведен функцией


class TestParsGoldApple(unittest.TestCase):

    def test_get_catalog_links(self):
        """
        Тест получения списка ссылок на заданной странице.
        Внимание!!! Тест может не проходить если какая-либо ссылка на странице изменилась.
        Чтобы тест прошел обновите список ссылок в переменной test_link
        """
        pga = ParsGoldApple()
        links = pga.get_catalog_links(settings.CATALOG, 1)
        test_link = ['https://goldapple.ru/19000201893-raffaello', 'https://goldapple.ru/19000051617-pour-lui', 'https://goldapple.ru/19000191526-magnolia-bouquet', 'https://goldapple.ru/19000041891-402-vanille-caramel-santal', 'https://goldapple.ru/19000148367-rose-magnetic', 'https://goldapple.ru/7192200018-miss-dior-blooming-bouquet', 'https://goldapple.ru/19000220691-winter-delicacies', 'https://goldapple.ru/19000241266-god-spirit', 'https://goldapple.ru/19000241269-holy-jasmine', 'https://goldapple.ru/19000257133-flawless131', 'https://goldapple.ru/19000004549-perfume-vanilla-blend', 'https://goldapple.ru/19000127039-happy-lemon-dulci', 'https://goldapple.ru/19000241268-mumbo-island', 'https://goldapple.ru/19000233252-sienna-brume', 'https://goldapple.ru/19000257139-surfer', 'https://goldapple.ru/19000220687-winter-pralines', 'https://goldapple.ru/19000122575-j-ai-l-air-de-ce-que-je-suis-j-r', 'https://goldapple.ru/19760327528-dylan-turquoise', 'https://goldapple.ru/19000122612-13-30-au-meme-endroit', 'https://goldapple.ru/19000009371-verte-euphorie', 'https://goldapple.ru/19000215889-803-embruns-gingembre-patchouli', 'https://goldapple.ru/19000225170-cuir-curcuma-deluxe-wood-coffret', 'https://goldapple.ru/19760302848-beaute-du-diable', 'https://goldapple.ru/82401200003-l-eau-d-hiver']
        self.assertEqual(links, test_link)

    def test_get_data_item(self):
        """
        Тест получения данных по ссылке
        """
        pga = ParsGoldApple()
        url = "https://goldapple.ru/19000201893-raffaello"
        data = pga.get_data_item(url)
        result = {'id': '19000201893', 'url': 'https://goldapple.ru/19000201893-raffaello', 'name': 'PANTHEON ROMA RAFFAELLO', 'price': '27300', 'currency': 'RUB', 'rate': '5.0', 'description': 'Он очень утонченный и эклектичный гений, в то же время сильный и конкретный. Профиль художника, сделавшего элегантность отличительной чертой своей работы. Изящество его штриха оставило неизгладимый след в истории искусства. Рафаэль —привлекательный, элегантный и страстный мужчина, полностью проживший свою историю любви. Обработка аромата проходит на двух уровнях: дистиллят чистого большого абсента и смесь перца, кожи, тикового дерева и бобов тонка. На первом уровне художник и его вибрация (абсент), на втором рассказывается вместо энергии (кожа, перец, тик и бобы тонка), с фоновым запахом, напоминающим цветные пигмент', 'instruction': 'Наносить на неповрежденные участки кожи, волос и одежду', 'made': 'страна происхождения: Италия; изготовитель:JOY S.P.A Via, del Lavoro 13, 61045, Pergola, Italy;'}
        self.assertEqual(data, result)
