import csv
from bs4 import BeautifulSoup
import requests
import services
import settings
from itemGoldApple import ItemGoldApple
import time


class ParsGoldApple:
    """ Класс для парсинга сайта """

    @staticmethod
    def get_catalog_links(catalog: str, page=1):
        """
        Процедура получает список ссылок записей
        :param page: Страница каталога для получения списка ссылок
        :param catalog: ссылка на каталог (без наименования домена, например: /catalog)
        :return: список ссылок на найденные позиции
        """
        links = []

        url = settings.URL_MAIN + catalog + f"?p={page}"
        response = requests.get(url)

        if response.status_code == 200:
            content = response.content.decode(settings.CODE_PAGE)
            bs = BeautifulSoup(content, "html.parser")
            temp = bs.find_all('a', settings.MASK_CATALOG_LINK)
            for link in temp:
                links.append(settings.URL_MAIN + link.get('href'))
        else:
            print(f'Ошибка при запросе {url}: {response.status_code}')
        return links

    @staticmethod
    def get_data_item(url: str):
        """
        Функция возвращает полученные данные в требуемом виде
        :param url: Ссылка на запись
        :return: Словарь с данными
        """
        data = None
        try:
            time.sleep(services.random_seconds(settings.TIME_LIMIT_ITEM))
            item = ItemGoldApple(url)
            data = {'id': item.get_item_id(), 'url': url, "name": item.get_item_name(), 'price': item.get_item_price(),
                    'currency': item.get_item_currency(), 'rate': item.get_item_rate(),
                    'description': item.get_item_description(), 'instruction': item.get_item_instruction(),
                    'made': item.get_item_made()}
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        return data

    @staticmethod
    def save_data(data: list, page: int):
        """
        Сохранить данные в CSV формате
        :param page: номер страницы для названия файла
        :param data: данные для записи
        :return: файл CSV с данными
        """
        f_name = 'data/' + settings.FILE_NAME + '-' + str(page) + settings.FILE_EXT
        with open(f_name, 'w', encoding=settings.FILE_CODEPAGE, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=settings.FIELDS_NAME, delimiter='|')
            writer.writeheader()
            writer.writerows(data)
