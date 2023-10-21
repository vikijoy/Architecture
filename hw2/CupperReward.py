from hw2.IGameItem import IGameItem

class CupperReward(IGameItem):
    def open(self):
        print("Открыли сундук с медью")