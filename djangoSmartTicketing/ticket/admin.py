from django.contrib import admin

import ticket
from ticket.models import TicketModel, UserTicketModel

admin.site.register(TicketModel)
admin.site.register(UserTicketModel)
