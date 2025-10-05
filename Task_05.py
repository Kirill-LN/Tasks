from datetime import datetime, timedelta

class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data.split()
        else:
            self.data = data

        self.future_data = None

    def validate(self):
        try:
            self.data = [int(x) for x in self.data]

            if not (1 <= self.data[0] <= 31):
                raise ('День должен быть от 1 до 31 ')
            if not (1 <= self.data[1] <= 12):
                raise ('Месяц должен быть от 1 до 12 ')
            if not (0 <= self.data[3] <= 23):
                raise ('Час должен быть от 1 до 23 ')
            if not (0 <= self.data[4] <= 59):
                raise ('Минуты должены быть от 0 до 59 ')
            if not (0 <= self.data[4] <= 59):
                raise ('Секунды должены быть от 0 до 59 ')
        except ValueError:
           print('Ошибка в формате ввода значений даты или времени')



    def convertTime(self):
        self.validate()

        data_str = f'{self.data[0]:02d}-{self.data[1]:02d}-{self.data[2]}'
        time_str = f'{self.data[3]:02d}:{self.data[4]:02d}:{self.data[5]:02d}'
        full_date_str = f'{data_str} {time_str}'

        self.data_obj = datetime.strptime(full_date_str, '%d-%m-%Y %H:%M:%S')

    def date_in_future(self, integer):
        try:
            days= int(integer)
            if hasattr(self, 'data_obj'):
                self.future_data = self.data_obj + timedelta(days=days)
            else:
                print("Сначала вызовите convertTime()")
        except ValueError:
            print("Введите корректное число дней")

    def output(self):

        self.convertTime()
        try:
            days_input = int(input('Введите количество дней: '))
            self.date_in_future(days_input)
            if self.future_data:
                print(self.future_data.strftime('%d-%m-%Y %H:%M:%S'))
        except ValueError:
            print(self.data_obj.strftime('%d-%m-%Y %H:%M:%S'))
            print("Ошибка ввода. Пожалуйста, введите целое число.")
            
Today_data = Data(input('Какая сейчас дата и время ? Введите в формате: день, месяц, год, час, минуты, секунды (пример: 10 12 2025 13 54): '))
Today_data.output()