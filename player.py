from PIL import Image, ImageTk


# Player object
class Player:
    def __init__(self, name = "", money=0, playerIconPath = '/Users/blairwarren/Desktop/ProjectBlake/defaultusericon.png'):
        self.name = name
        self.money = money
        self.playerIconPath = playerIconPath
        self.playerIconPath
        self.icon = ImageTk.PhotoImage(Image.open(playerIconPath).resize((50, 50)))
        
    
    def updatePlayerInfo(self, name, money, playerIconPath):
        self.name = name
        self.money = money
        self.playerIconPath = playerIconPath
        self.icon = ImageTk.PhotoImage(Image.open(playerIconPath).resize((50, 50)))
        