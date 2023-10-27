import icontract


class CashProvider:
    __card_num: str
    __isAuthorized: bool

    def __init__(self, card_num):
        self.__card_num = card_num
        self.isAuthorized = False

    def getCardNum(self):
        return self.__card_num

    def setCardNum(self, card_num):
        self.__card_num = card_num

    @icontract.require(lambda self: int(self.getCardNum()) % 10 > 5)
    def authorize(self):  # Попытка запилить контракт с предусловием.
        # Авторизуем карту при условии, что последняя цифра больше 5
        self.isAuthorized = True
        print(f'Карта подтверждена: {self.__card_num}')

    def getAuth(self):
        return self.isAuthorized

    def __repr__(self):
        return f"CashProvider(card_num: {self.__card_num}, isAuthorized: {self.isAuthorized})"