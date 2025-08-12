
from numpy import number

class ListFilter:
    def __init__(self):
        self.input_list = list( input('Введите числа через пробел:').split())
        self.input_range_list = list( input('Введите диапазон:').split())

        self.filter_list = []
        self.range_list = []
        self.results = []


    def filter_input(self):
        print(f"Исходный список: {self.input_list}")
        for item in self.input_list:
            try:
                number = int(item)
                self.filter_list.append(number)
            except ValueError:
                continue
        print(f"Отфильтрованный список: {self.filter_list}")
        return self.filter_list

    def len_verify_range(self):
        print(f"Проверка диапазона: {self.range_list}")
        if len(self.range_list) != 2 :
            print('Диапазон должен состоять из 2-х чисел')

    def verify_type(self):
        try:
            self.range_list = [int(num) for num in self.input_range_list]

            if not all(isinstance(num,int) for num in self.range_list):
                raise TypeError("Все числа диапазона должны быть целыми!")

        except ValueError as e:
            print('Ошибка :' , e )

        else:
            print(f"Проверенный диапазон: {self.range_list}")  # Отладка
            return self.range_list

    def coincidence(self):
        self.filter_input()
        self.range_list = self.verify_type()
        self.len_verify_range()

        print(f"Проверка входных данных: {self.input_list}, {self.input_range_list}")
        if not self.input_list or not self.range_list:
            return []

        self.coincidence_list = list(range(self.range_list[0], self.range_list[1]))
        print(f"Список совпадений: {self.coincidence_list}")

        for number in self.filter_list:
            if number in self.coincidence_list:
                self.results.append(number)
        print(f"Финальный результат: {self.results}")
        return self.results


list1 = ListFilter()

try:
    result = list1.coincidence()
    print('Новый список :' , result)
except (ValueError,TypeError) as e:
    print('Ошибка : ' , e)