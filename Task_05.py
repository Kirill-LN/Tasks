from datetime import datetime
from datetime import timedelta

class Date:
    def __init__(self):
        """
        Функция инициализируе нынешнюю дату
        """
        self.today = datetime.now()

    def getDate(self, format = '%d/%m/%Y %H:%M:%S'):
        """
        Возвращает текущую дату в заданном формате
        По умолчанию: 'дд/мм/гггг ЧЧ:ММ:СС'
        """
        try:
            return self.today.strftime(format)
        except:
            return ('Ошибка при вводе данных')

    def date_in_future(self, integer):
        """
        Принимает на ввод количество дней которые прибавляет к сегодняшней датеи времени
        Выводит дату которая получилась послесложения
        Если введено неверно число выводит сегодняшнюю дату и просит написать целое число исправив ошибку
        """
        try :
            days = int(integer)
            self.future_date = self.today + timedelta(days=days)
        except ValueError:
            print ('Введите корректное число дней')

    def output(self):
        try:
            day_input= int(input('На сколько дней прибавим? :'))
            self.date_in_future(day_input)
            if self.future_date :
                print (self.future_date.strftime('%d/%m/%Y %H:%M:%S'))
        except ValueError:
                print (self.today.strftime('%d/%m/%Y %H:%M:%S'))
                print ('Введите целое число')

today= Date()
today.output()
