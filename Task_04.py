class Sort:
    def __init__(self, list):
        self.list = list

        self.list_only_num = []

    def verify_type(self):
        """Фильтрует список, оставляя только числа"""
        for num in self.list:
            try:
                # Преобразуем в число и добавляем в отфильтрованный список
                num = int(num)
                self.list_only_num.append(num)
            except (ValueError, TypeError):
                # Пропускаем элементы, которые нельзя преобразовать в число
                continue
        return self.list_only_num


    def sort_list(self):
        # Фильтруем числа
        self.verify_type()

        # Проверяем, есть ли числа для обработки
        if not self.list_only_num:
            return []

        # Находим максимальное и минимальное значения
        max_value = max(self.list_only_num)
        min_value = min(self.list_only_num)

        result = []

        for num in self.list_only_num:
            if num == max_value:
                result.append(min_value) # меняем max на min
            elif num == min_value: # меняем min на max
                result.append(max_value)
            else:
                result.append(num) # остальные числа оставляем
        result.append(min_value)
        return result

user_list = Sort(input('Введите список через пробел : '))
result = user_list.sort_list()
print(result)