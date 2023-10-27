from datetime import datetime
from typing import List

from Ticket import Ticket


class TicketProvider:

    def updateTicket(self, ticket: Ticket):
        res = True
        if ticket.getDate() < datetime.now().date():
            ticket.set_is_valid(False)
            print(f'Билет {ticket} не годен')
            res = False
        else:
            print(f'Билет {ticket} годен')
        return res

    def getTicket(self, num, tickets: List[Ticket]) -> bool:
        res = False
        for ticket in tickets:
            if ticket.getSerialNumber() == num:
                res = True
                break
        return res