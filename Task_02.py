class ListFilter:

    def __init__(self):
        self.input_list= list(map(int, input('Введите числа через пробел:').split()))
        self.new_list = []

   # def - сделать проверку на тип данных

    def coincidence(self, range):
        range_list = list(range)
        for num in self.input_list:
            if num in range_list:
                self.new_list.append(num)
        return self.new_list

filter = ListFilter()
# сделать так что бы range работал через input
filtered_list = filter.coincidence(range(input(map(int))))
print('Новый список : ' , filtered_list)


