class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        return self.count + v <= self.capacity
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v):
            self.count += v
        # положить v монет в копилку