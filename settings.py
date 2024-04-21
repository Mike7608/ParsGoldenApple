# Основные настройки программы
START_PAGE = 23
END_PAGE = 25
CODE_PAGE ='utf-8'
URL_MAIN = "https://goldapple.ru"
URL_RATE = '/review/product'
CATALOG = '/parfjumerija'
TIME_LIMIT_PAGE = 100
TIME_LIMIT_ITEM = 2
# Настройки для поиска данных
MASK_CATALOG_LINK = {'itemprop': 'url', 'class': 'bp0xn d+d4r QfHm9 +6yOX'}
MASK_ID_ITEM = {'itemprop': 'sku'}
MASK_NAME_ITEM = {'value': 'Description_0', 'text': 'описание'}
MASK_CURRENCY_ITEM = {'itemprop': 'priceCurrency'}
MASK_PRICE_ITEM = {'itemprop': 'offers', 'itemscope': 'itemscope'}
MASK_DESCRIPTION_ITEM = {'value': 'Description_0', 'text': 'описание'}
MASK_INSTRUCTION_ITEM = [{'text': 'применение'}, {'class': 'oAN8f'}]
MASK_MADE_ITEM = {'text': 'Дополнительная информация'}
# Настройки для сохранения данных
FILE_NAME = "parfjumerija"
FILE_EXT = '.csv'
FILE_CODEPAGE = "UTF-8"
FIELDS_NAME = ["id", 'url', 'name', 'price', "currency", "rate", "description", "instruction", 'made']
