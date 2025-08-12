
from numpy import number

class ListFilter:
    def __init__(self):
        self.input_list = list( input('Введите числа через пробел:').split())
        self.range_list = list(map(int, input('Введите диапозон:').split()))

        self.filter_list = []
        self.results = []

    def process_list(self):
        if not self.input_list and not self.range_list:
            return []
        return self.filter_list

    def filter_input(self):
            for item in self.input_list:
                try:
                    number = int(item)
                    self.filter_list.append(number)
                except ValueError:
                    continue
            return self.filter_list

    def len_verify_range(self):
        if len(self.range_list) != 2 :
            print('Диапозон должен состоять из 2-х чисел')

    def verify_type(self):

        if not all(isinstance(number, int) for number in self.range_list):
            raise TypeError('Все числа диапозона должны быть целыми')


    def coincidence(self):
        if not self.input_list or not self.range_list:
            return []

        self.filter_input()
        self.len_verify_range()
        self.verify_type()

        self.coincidence_list = list(range(self.range_list[0], self.range_list[1]))

        for number in self.filter_list:
            if number in self.coincidence_list:
                self.results.append(number)
        return self.results


list1 = ListFilter()

try:
    result = list1.coincidence()
    print('Новый список :' , result)
except (ValueError,TypeError) as e:
    print('Ошибка : ' , e)