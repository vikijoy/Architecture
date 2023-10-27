from datetime import datetime
from typing import List

from HW4.CashProvider import CashProvider
from HW4.Ticket import Ticket
from random import choices

from HW4.TicketProvider import TicketProvider


class Customer:
    __base_id = 1
    __id: int
    __tickets: list[Ticket] = [Ticket()]
    __cash_provider: CashProvider
    __ticket_provider: TicketProvider

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__id = cls.__base_id
        cls.__base_id += 1
        return instance

    def __init__(self):
        self.__cash_provider = CashProvider(''.join(choices('0123456789', k=16)))
        self.__ticket_provider = TicketProvider()
        self.__tickets = [Ticket() for i in range(1, 101)]

    def __repr__(self):
        return (f"Customer(id: {self.__id},\n"
                f"tickets:\n"
                f"  {self.__tickets},\n"
                f"cash_provider: {self.__cash_provider}")

    def getTicketProvider(self):
        return self.__ticket_provider

    def getTickets(self):
        return self.__tickets

    def getCashProvider(self):
        return self.__cash_provider

    def setCashProvider(self, cash_provider: CashProvider):
        self.__cash_provider = cash_provider

    def buyTicket(self, ticket: Ticket):
        res = False
        if (self.getCashProvider().getAuth() and
                self.getTicketProvider().getTicket(ticket.getSerialNumber(), self.getTickets()) and
                self.getTicketProvider().updateTicket(ticket)):
            print(f'Покупка билета:{ticket}')
            res = True
        return res

    def searchTicket(self, date: datetime.date, tickets: List[Ticket]) -> List[Ticket]:
        res = []
        for ticket in tickets:
            if ticket.getDate() == date:
                res.append(ticket)
        return res