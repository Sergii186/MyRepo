from random import randint

class Randomizer:
    def __init__(self):
        self.begin_num = None
        self.end_num = None
    
    def generate(self, begin, end):
        self.begin_num = begin
        self.end_num = end
        return randint(self.begin_num, self.end_num)

# Створення об'єкта класу Randomizer
randomizer = Randomizer()

# Виклик методу generate з двома аргументами
result = randomizer.generate(10, 20)

# Виведення результату
print(result)
