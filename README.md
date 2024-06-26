# ParsGoldenApple
Утилита парсинга сайта https://goldapple.ru/parfjumerija

## Описание

Есть сайт https://goldapple.ru/parfjumerija со списком товаров, рейтингом, условиями его применения и прочей информацией, которая помогает пользователю сделать выбор при покупке.



### Задача

<aside>
👾 Задача: создать CSV файл со всеми товарами магазина.

В этом файле должна быть следующая информация в текстовом формате:

1. ссылка на продукт
2. наименование
3. цена
4. рейтинг пользователей
5. описание продукта
6. инструкция по применению
7. страна-производитель
</aside>

### Требуемый стэк

- python 3.11

### Условия приемки

- код размещен в открытом репозитории
- код покрыт тестами минимум на 75%
- доступна документация
- код оформлен согласно pep8
- оформлен Readme файл
- `итоговая выгрузка в виде файла приложена к Readme`

### От автора

Небольшая утилита для парсинга сайта создана как дипломный проект skypro: Профессия Python-разработчик.

Стандартно утилита имеет настройки для получения всех требуемых данных по заданной ссылке.
Данная утилита состоит из следующих файлов и папок:
- папка data - в ней сохраняются файлы с данные в формате csv.
- settings.py - файл с настройками
- services.py - файл с доп. сервисными утилитами
- requirements.txt - требуемые пакеты для установки
- README.md - описание
- parsGoldApple.py - общий файл класс для получения и записи данных
- itemGoldApple.py - файл класс для работы с одной записью полученных данных
- main.py - главный запускаемый файл для получения данных как пример работы
- tests.py - unittest-ы для тестирования функций приложения (согласно условию задания)

Теперь немного о настройках в файле 
### settings.py:
#### Основные настройки программы
    START_PAGE = 1 - начальная страница 
    END_PAGE = 500 - кончаная страница
    CODE_PAGE ='utf-8' - кодировка данных
    URL_MAIN = "https://goldapple.ru" - домен сайта
    URL_RATE = '/review/product' - ссылка для получения рейтинга
    CATALOG = '/parfjumerija' - требуемый каталог для парсинга 
    TIME_LIMIT_PAGE = 100 - прилизительная задержка для получения страниц в сек.
    TIME_LIMIT_ITEM = 2 - приблизительная задержака для получени данных со страниы в сек.
#### Настройки для поиска данных
    MASK_CATALOG_LINK = {'itemprop': 'url', 'class': 'bp0xn d+d4r QfHm9 +6yOX'} - маска поиска ссылки позиции товара на странице
    MASK_ID_ITEM = {'itemprop': 'sku'} - маска поиска кода/артикула изделия 
    MASK_NAME_ITEM = {'value': 'Description_0', 'text': 'описание'} - маска поиска наименования изделия
    MASK_CURRENCY_ITEM = {'itemprop': 'priceCurrency'} - маска поиска валюты изделия
    MASK_PRICE_ITEM = {'itemprop': 'offers', 'itemscope': 'itemscope'} - маска поиска цены изделия
    MASK_DESCRIPTION_ITEM = {'value': 'Description_0', 'text': 'описание'} - маска поиска описания изделия
    MASK_INSTRUCTION_ITEM = [{'text': 'применение'}, {'class': 'oAN8f'}] - маска поиска инструкции изделия
    MASK_MADE_ITEM = {'text': 'Дополнительная информация'} - маска поиска производителя изделия
#### Настройки для сохранения данных
    FILE_NAME = "parfjumerija" - название файла для записи данных
    FILE_EXT = '.csv' - тип файла
    FILE_CODEPAGE = "UTF-8" - кодировка файла
    FIELDS_NAME = ["id", 'url', 'name', 'price', "currency", "rate", "description", "instruction", 'made'] - какие данные и в каком порядке нужно сохранять (на данный момент этот параметр не изменять!!!)


### parsGoldApple.py:
На текущий момент файл имеет всего 3 функции:

    get_catalog_links(catalog, page)
        Процедура получает список ссылок записей
        Параметр page: Страница каталога для получения списка ссылок
        Параметр catalog: ссылка на каталог (без наименования домена, например: /catalog)
        Результат: список ссылок на найденные позиции

    get_data_item(url):
        Функция возвращает полученные данные в требуемом виде одной записи
        Параметр url: Ссылка на запись
        Результат: Словарь с данными

    save_data(data, page):
        Сохранить данные в CSV формате
        Параметр page: номер страницы для названия файла
        Параметр data: данные для записи
        Результат: файл CSV с данными

### itemGoldApple.py:

Данный файл содержит класс для работы с одной записью данных. При инициализации передается ссылка на запись которую нужно получить.
Вот описание процедур:

    __init__(url): - инициализатор класса. Принимает ссылку для получения данных только на 1 позицию
    __str__ - информациооный
    __repr__ - информациооный
    get_item_rate - возвращает рейтинг
    get_item_id - возврашает код/артикул
    get_item_name - возвращает наименование
    get_item_price - возвращает цену
    get_item_currency - возвращает валюту
    get_item_description - возвращает описание
    get_item_instruction - возвращает инструкцию
    get_item_made - возвращает страну происхождения и производителя


### services.py
Здесь пока только одна функция random_seconds для получения случайного времени в секундах. Принимает 1 параметр - это секунды для задержки. На выходе немного увеличенное рандомное время в секундах.

### main.py
Главный запускаемый файл для получения данных как пример работы.
Если запустить, сразу начнется парсинг заданного магазина (каталога).
По умолчанию заданы параметры для получения всех данных. Эти параметры можно изменить в файле settings.py.
После запуска будет выведена некоторая информация в консоль для информирования о проделанной работе.
Пример:

    *******************************************
    *   Получаем список записей страницы 1    *
    *******************************************
    *********************************************
    *   Страница: 1, записей на странице: 24    *
    *********************************************
    1 (1) https://goldapple.ru/19760330470-live-free
    2 (2) https://goldapple.ru/19000153642-fraise-bonbon
    3 (3) https://goldapple.ru/7360100003-5th-avenue
    ...

Здесь консоль информирует о получении списка ссылок на заданной странице и сколько записей (ссылок) на ней найдено. Затем идет загрузка данных по полученным ссылкам. Постепенно в списке появляются ссылки по которым идет выборка дынных. Первая цифра в строке указывает на порядковый номер общего количества полученных записей. Второе чисто (в скобках) указывает на порядковый номер в текущем списке.

После полной выборки списка с текущей страницы будет выведено информациюнное сообщение, что данные получены и сохранены в файл успешо.
Пример:

    694 (22) https://goldapple.ru/19000231614-wood-leather
    695 (23) https://goldapple.ru/26480200006-opulent-silver
    696 (24) https://goldapple.ru/19000061646-effusion-for-him
    ************************************************************************
    *   Данные страницы 29 сохранены в файл parfjumerija-29.csv успешно!   *
    ************************************************************************

Если ещё не все страницы выбраны, тогда будет предложено немного подождать, пример:

    ***********************
    *   Ждем 100 секунд   *
    ***********************

После чего начнется загрузка и обработка следующей страницы.
Если будут выбраны все заданные страницы программа завершит работу. Об этом будет выведено следующее сообщение:

    ********************************************************************
    *    Все заданные страницы выбраны! Программа завершила работу.    *
    ********************************************************************

## Внимание!!!
После каждой полученной страницы данных, автоматически создается файл с названием заданным в настройках, и номером страницы как префикс к названию файла. Файлы хранятся в папке /data/. Каждый файл хранит только ту страницу данных в наименование которого указано число как префикс. Например: parfjumerija-1.csv имеет префикс 1 (значит хранит данные со страницы 1). Наприимер: если на сайте будет 500 страниц - значит будет создано 500 фалов с данными. 
На мой взгляд так больше всего вероятность получить эти данные :).

Ссылка на файлы для примера: https://github.com/Mike7608/ParsGoldenApple/blob/main/data

И ещё: согласно задания требуется получить взе записи с сайта. Так как это очень большой объём данных по обработке занимает продолжительное время, если уж точно нажны все данные тогда придется запустить утилиту(программу) и слить все требуемые данные )). На момент написания данного текста произошли изменения в данных сервера сайта. Некоторые маски придется поправлять.

Например: в данном материале в настройках программы (раздел Настройки для поиска данных) указана маска для посика ссылок следующая: 

    MASK_CATALOG_LINK = {'itemprop': 'url', 'class': 'bp0xn d+d4r QfHm9 +6yOX'}

На текущий момент наименование class-а изменилось. Для получения ссылок работает маска: 

    MASK_CATALOG_LINK = {'itemprop': 'url', 'class': 'znh2x rUS0k X1PzR Y63OX'}

Скорость получения данных составляет примерно 1 страница 7-8 минут.