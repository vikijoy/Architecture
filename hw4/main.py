from datetime import datetime, timedelta
from random import choices, randint
import icontract
from Customer import Customer

if __name__ == '__main__':
    print('Проверка авторизации:')
    customer = Customer()
    print(f'Весь объект:\n{customer}')

    cp = customer.getCashProvider()
    print(f'До авторизации: {cp.getAuth()}')
    while not cp.getAuth():
        try:
            cp.authorize()
        except icontract.ViolationError:  # Контракт вызывает исключение при невыполнении условий
            print('Карта не подтверждена')
            cp.setCardNum(''.join(choices('0123456789', k=16)))
            print(cp)
    print(f'После авторизации: {cp.getAuth()}')

    print('Проверка билетов:')
    tickets = customer.getTickets()

    print(f'Поиск билетов:\n')
    search_ticket = (customer.searchTicket((datetime.now() + timedelta(days=10)).date(), tickets))
    if search_ticket:
        print(search_ticket)

    print(f'Покупка билета:')
    for i in range(len(tickets)):
        buy_ticket = customer.buyTicket(tickets[i])
        if buy_ticket:
            print(buy_ticket)
            break