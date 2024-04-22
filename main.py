import time
import services
import settings
from parsGoldApple import ParsGoldApple


def print_info(info):
    """ Для вывода информации """
    print("*" * (len(info) + 8))
    print("*   " + info + "   *")
    print("*" * (len(info) + 8))


def get_one_item(link):
    """
    Процедура получения данных одной записи согласно настроек settings.py
    :param link: ссылка на позицию которую требуется получить
    :return: Вывод на экран данных в виде словаря
    """
    pga = ParsGoldApple()
    d = pga.get_data_item(link)
    print(d)


def get_all_items():
    """
    Процедура получения всех данных согласно настроек settings.py
    :return: Файл(ы) с данными в |data|
    """
    pga = ParsGoldApple()

    for page in range(settings.START_PAGE, settings.END_PAGE):
        # резервируем переменную для хранения полученных данных
        data = []
        # получаем список ссылок на изделия с заданной страницы
        print_info(f"Получаем список записей страницы {page}")
        links = pga.get_catalog_links(settings.CATALOG, page=page)
        # небольшая задержка для спокойствия сервера :)

        # получаем количество записей (ссылок) на странице
        len_list = len(links)
        # счетчик записей
        number = (page * len_list) - len_list
        # выводим небольшую информацию по текущй странице
        print_info(f"Страница: {page}, записей на странице: {len_list}")

        # если список не пустой - запускаем цикл получения данных по каждой позиции
        if len(links) > 0:
            for link in links:
                number += 1
                # выводим информацию о текущей позиции
                print(number, f'({number - (page * len_list) + len_list})', link)
                # получаем данные по текущей позиции
                temp = pga.get_data_item(link)
                # сохраняем данные в зарезервированной переменной
                data.append(temp)

            # после окончания цикла передаем все данные для записи в файл
            pga.save_data(data, page)

            print_info(f'Данные страницы {page} сохранены в файл {settings.FILE_NAME + "-" + str(page) + settings.FILE_EXT} успешно!')

            sec = services.random_seconds(settings.TIME_LIMIT_PAGE)
            print_info(f"Ждем {round(sec)} секунд")
            time.sleep(sec)
        else:
            print_info("Нет данных!")
            break

    print_info('Все заданные страницы выбраны! Программа завершила работу.')


def main():

    # get_one_item('https://goldapple.ru/19000201893-raffaello')

    get_all_items()


if __name__ == '__main__':
    main()
