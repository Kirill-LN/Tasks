class Maximum_odd():
    def __init__(self):
        self.user_input_string= list(input('Введите значения через пробел :').split())

        self.only_num_string = []
        self.odd_numbers = []

    def verify_type(self):
        '''
        Метод верификации входных значений и преобразования их в тип float
        Возвращает: список в котором только целые числа, пропуская буквы и символы
        В случае если пользователь не ввел значений возвращает ошибку
        '''
        if not self.user_input_string:
            raise TypeError('Строка не должна быть пустой, введите значения')

        for item in self.user_input_string:
            try:
                item = float(item)
                if item.is_integer():
                    self.only_num_string.append(item)
            except (ValueError, TypeError):
                continue
        return self.only_num_string

    def find_max_odd(self):
        '''
        Метод для поиска максимального нечетного числа
        Возвращает: максимальное нечетное число или None
        '''

        self.verify_type()

        for num in self.only_num_string:
            if num % 2 != 0 and num >= 0:
                self.odd_numbers.append(int(num))

        if self.odd_numbers:
            return max(self.odd_numbers)
        else:
            return None

user_string = Maximum_odd()
max_odd = user_string.find_max_odd()

if max_odd == None :
    print(None)
else:
    print(f'Максимальное нечетное число : {max_odd}')

