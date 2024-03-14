from django.contrib import admin

import ticket
from ticket.models import TicketModel

admin.site.register(TicketModel)