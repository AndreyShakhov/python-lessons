class Buffer:
    def __init__(self):
        self.sequence_elements = []
        '''конструктор без аргументов'''

    def add(self, *a):
        self.sequence_elements.extend(a)
        while len(self.sequence_elements) <= 5:
            print(sum(self.sequence_elements))
            self.sequence_elements = self.sequence_elements[5::]


        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.sequence_elements
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены