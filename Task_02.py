
class Span:
    def __init__(self):
        self.input_list = list( input('Введите числа через пробел:').split())
        self.input_range_list = list( input('Введите диапазон:').split())

        self.list_only_num = []
        self.range_list = []
        self.results = []

    def verify_type_list(self):

        for num in self.input_list:
            try:
                num = int(num)
                self.list_only_num.append(num)
            except ValueError:
                continue
        return self.list_only_num

    def verify_type_rangelist(self):
        try:
            self.range_list = [int(num) for num in self.input_range_list]
            return True

        except ValueError as e:
            return False

    def len_verify_range(self):
        if len(self.range_list) != 2 :
            return False
        return True

    def coincidence_list(self):
        if len(self.range_list) != 2:
            return []

        start, end = self.range_list
        return  [num for num in self.list_only_num if start <= num <= end]


    def coincidence(self):
        if (self.verify_type_list() and
        self.verify_type_rangelist() and
        self.len_verify_range()):

            self.results = self.coincidence_list()

        print (f'Финальный список : {self.results}')

list1 = Span()
list1.coincidence()