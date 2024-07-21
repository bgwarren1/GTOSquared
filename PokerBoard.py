


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def playerTag(self):
        return self.name + ': ' + self.money
    

p1 = Player('Beans', 100)
print(p1.money)