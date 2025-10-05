class Span:
    def __init__(self,input_list = None, input_range_list = None ):
        self.input_list = input_list
        self.input_range_list = input_range_list

        self.list_only_num = []
        self.range_list = []
        self.results = []

    @property
    def input_list(self):
        return self._input_list

    @input_list.setter
    def input_list(self,value):
        self._input_list = value

    @property
    def input_range_list(self):
        return self._input_range_list

    @input_range_list.setter
    def input_range_list(self,value):
        self._input_range_list = value

    def get_user_input(self):
        '''
        Метод получения значений списка и интервала от пользователя
        '''
        try :
            user_input_str = input('Введите значения через пробел :')
            self.input_list = user_input_str.strip().split()

            user_range_input = input('Введите значения интервала через пробел:')
            self.input_range_list = user_range_input.strip().split()

        except Exception as e:
            print(f'Произошла ошибка при вводе данных: {e}')

    def verify_type_list(self):
        '''
        Метод верификации входных значений списка и преобразования их в тип int пропуская буквы
        Возвращает : список в котором только вещественные числа
        '''

        self.list_only_num = []

        if not self.input_list:
            return self.list_only_num

        for num in self.input_list:
            try:
                num = int(num)
                self.list_only_num.append(num)
            except ValueError:
                continue
        return self.list_only_num

    def verify_type_rangelist(self):
        '''
        Метод верификации входных значений интервала и преобразование их в тип int
        Возвращает: интервал с вещественными числами или, в случае если в интервале буква или символ, ошибку
        '''

        if not self.input_range_list:
            return []

        try:
            self.range_list = [int(num) for num in self.input_range_list]
            return self.range_list

        except ValueError :
            print('Все значения интервала должны быть числами')
            return None

    def len_verify_range(self):
        '''
        Метод проверки интервала на количество значений
        В случае если кол-во значений интервала не равно 2, возвращает пустой список
        '''

        if len(self.range_list) != 2 and len(self.input_range_list) != 2 :
            print("Интервал должен содержать ровно два числа")
            return []
        return self.range_list

    def coincidence(self):
        '''
        Метод поиска совпадений
        '''

        if (self.verify_type_list() and
            self.verify_type_rangelist() and
            self.len_verify_range()):

            start, end = self.range_list
            self.results = [num for num in self.list_only_num if start <= num <= end]
            print(self.results)
            return self.results

        else:
            self.results = []
            print(f'Ошибка при вводе данных или пустой ввод : {self.results}')

try :
    list1 = Span()
    list1.get_user_input()
    list1.coincidence()
except Exception as e:
    print(f'Произошла ошибка : {e}' )