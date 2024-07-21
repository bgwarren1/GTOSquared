from PIL import Image, ImageTk


# Player object
class Player:
    def __init__(self, name, money, playerIcon):
        self.name = name
        self.money = money
        
    
    def playerTag(self):
        return self.name + ': ' + self.money
    




playerList = [] # List of players

# Adding new players
def addPlayer(name, money):
    player = Player(name, money)
    playerList.append(player)




