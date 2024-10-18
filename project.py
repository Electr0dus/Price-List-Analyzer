import operator
import os
import csv

class PriceMachine():
    __name_product: list = ['название', 'продукт', 'товар', 'наименование']
    __name_price: list = ['цена', 'розница']
    __name_weight: list = ['фасовка', 'масса', 'вес']

    def __init__(self):
        self.result = ''
        self.name_length = 0
        self.all_data_product = []  # Создаём словарь для записи в файл JSON

    def load_prices(self, file_path=''):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        # Сканирую каталог на наличие файлов и если найден с указанным именем добавляю в список self.data[]
        self.data = [file for file in os.listdir(file_path) if 'price' in file]
        # Делаем перебор по всем файлам .csv всех значений и сохраняем их в словарь
        for data in self.data:
            # Используем параметр объекта self.name_length = 0 для хранения номера строки всех данных файлов CSV
            with open(f'prices/{data}', encoding='utf-8') as file_csv:
                _index_product = 0  # Хранит значение индекса наименования товара с продуктами
                _index_price = 0  # Хранит значение индекса  товара с ценой
                _index_weight = 0  # Хранит значение индекса веса товара
                file_reader = csv.reader(file_csv, delimiter=',')
                # Найти индексы значений и сохранить их
                for index_data in file_reader:
                    for ind in index_data:
                        if ind in self.__name_product:
                            _index_product = index_data.index(
                                ind)  # Записать текущий индекс для вывода данных название товара
                        elif ind in self.__name_price:
                            _index_price = index_data.index(
                                ind)  # Записать текущий индекс для вывода данных цены товара
                        elif ind in self.__name_weight:
                            _index_weight = index_data.index(
                                ind)  # Записать текущий индекс для вывода данных веса товара
                    break
                for row in file_reader:
                    self.name_length += 1  # Увелечения номера по порядку
                    # Записать данные в словарь для дальнейшей сериализации в JSON файл
                    price_for_kg = f'{int(row[_index_price]) / int(row[_index_weight]):.2f}'
                    self.all_data_product.append([self.name_length, row[_index_product], row[_index_price],
                                                  row[_index_weight], data, float(price_for_kg)])

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        # Отсортировать данные по возрастанию цены за кг
        data_sorted = sorted(self.all_data_product, key=operator.itemgetter(5))
        for number, item in enumerate(data_sorted):
            # [461, 'Филе пангасиуса б/ш ', '92', '1', 'price_5.csv', 92.0]
            value, product_name, price, weight, file_name, price_for_kilo = item
            result += '<tr>'
            result += f'<td>{number + 1}</td>'
            result += f'<td>{product_name}</td>'
            result += f'<td>{price}</td>'
            result += f'<td>{weight}</td>'
            result += f'<td>{file_name}</td>'
            result += f'<td>{price_for_kilo}</td>'
            # result += '<br>'
        with open(fname, mode='w') as file_html:
            file_html.write(result)

    def find_text(self, text: str = ''):
        data_request: list = []  # Хранит данные товаров запрошенные пользователем
        # Сформировать список с необходимыми данными
        for req in self.all_data_product:
            if text.lower() in req[1].lower():
                data_request.append(req)
        # Сформировать сортированный список по возрастанию цены за кг
        data_request = sorted(data_request, key=operator.itemgetter(5))
        # Вывод данных в консоль внеобходимой форме
        print(f'{"№":<3} {"Наименование":<45}{"цена":<8}{"вес":<5}{"файл":<15}{"цена за кг.":<10}')
        count_product = 1  #Для вывода значения количества продукта по порядку
        for product in data_request:
            print(f'{count_product:<3} {product[1]:<45}{product[2]:<8}{product[3]:<5}{product[4]:<15}{product[5]:<10}')
            count_product += 1


pm = PriceMachine()
pm.load_prices('prices')
'''
    Логика работы программы
'''
request_user = input('Введите название товара ("exit" для выхода): ')
while request_user.lower() != 'exit':
    pm.find_text(request_user)
    request_user = input("Введите название товара (exit для выхода): ")
print('the end')
pm.export_to_html('my_file.html')
