import requests
from bs4 import BeautifulSoup
import settings


class ItemGoldApple:
    """
    Класс для работы с одной записью данных
    В класс при инициализации передается ссылка на запись которую нужно получить.

    """

    def __init__(self, url):
        """
        Инициализатор класс. После инициализации в классе хранятся полученные данные
        :param url: ссылка на запись для получения данных
        """
        self.url = url
        self.response = requests.get(url)
        self.response_rate = None
        if self.response.status_code == 200:
            self.content = self.response.content.decode(settings.CODE_PAGE)
            self.bs = BeautifulSoup(self.content, "html.parser")
            self.id_item = self.bs.find('meta', settings.MASK_ID_ITEM).get('content')
            self.response_rate = requests.get(settings.URL_MAIN + settings.URL_RATE + '/' + self.id_item)
        else:
            print(f'Ошибка при запросе {url}: {self.response.status_code}')

    def __str__(self):
        return (f'id: {self.id_item}, '
                f'url: {self.url}, '
                f'name: {self.get_item_name()}, '
                f'price: {self.get_item_price()}, '
                f'currency: {self.get_item_currency()}, '
                f'rate: {self.get_item_rate()}, '
                f'description: {self.get_item_description()}, '
                f'instruction: {self.get_item_instruction()}, '
                f'made: {self.get_item_made()}')

    def __repr__(self):
        return self.__str__()

    def get_item_rate(self):
        """
        Функция возвращает рейтинг записи
        :return: рейтинг
        """
        rate = None
        if self.response_rate.status_code == 200:
            content = self.response_rate.content.decode(settings.CODE_PAGE)
            bs = BeautifulSoup(content, "html.parser")

            rate = bs.find("div", {'itemprop': 'ratingValue'})

            if rate:
                rate = rate.text.strip()
            else:
                rate = None
        else:
            print(f'Ошибка при запросе рейтинга {self.url}: {self.response_rate.status_code}')
        return rate

    def get_item_id(self):
        """
        :return: Код/артикул записи
        """
        return self.id_item

    def get_item_name(self):
        """
        :return: Наименование
        """
        name = self.bs.find('div', settings.MASK_NAME_ITEM)
        if name:
            value = name.contents[0].text.strip()
            return value

    def get_item_price(self):
        """
        :return: Цена
        """
        temp = self.bs.find('div', settings.MASK_PRICE_ITEM)
        if temp:
            price = temp.find('meta', {'itemprop': 'price'}).get('content')
            return str(price)

    def get_item_currency(self):
        """
        :return: Валюта изделия
        """
        currency = self.bs.find('meta', settings.MASK_CURRENCY_ITEM).get('content')
        if currency:
            return str(currency)

    def get_item_description(self):
        """
        :return: Описание
        """
        description = self.bs.find('div', settings.MASK_DESCRIPTION_ITEM)
        value = None
        if description:
            value = description.contents[4].text.replace('\n', '*').strip()
        return value

    def get_item_instruction(self):
        """
        :return: Инструкция
        """
        target_div1 = self.bs.find('div', settings.MASK_INSTRUCTION_ITEM[0])

        instruction = None
        if target_div1:
            value = target_div1.find('div', settings.MASK_INSTRUCTION_ITEM[1])
            if value:
                instruction = value.text.strip().replace('\n', '*')
        return instruction

    def get_item_made(self):
        """
        :return: Производитель
        """
        target_div2 = self.bs.find('div', settings.MASK_MADE_ITEM)

        if target_div2:

            made_temp = target_div2.find('div')

            if made_temp.contents:

                temp = ''

                for item in made_temp:
                    t = str(item)
                    if t == '<br>' or t == '<br/>':
                        continue

                    if t == 'страна происхождения':
                        temp += t + ': '
                        continue
                    elif t == 'изготовитель:':
                        temp += t
                        continue
                    else:
                        temp += t + '; '

                return temp.strip()

            else:

                return None

        else:
            return None
