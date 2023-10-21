from hw2.ItemFabric import ItemFabric
from hw2.GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (др. камень)")
        return GemReward()