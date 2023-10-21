from hw2.ItemFabric import ItemFabric
from hw2.SilverReward import SilverReward


class SilverGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (серебро)")
        return SilverReward()