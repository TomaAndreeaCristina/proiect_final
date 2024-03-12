from django.urls import path
from servicii.views import ServiciiUpdateView, ServiciiCreateView, ServiciiDeleteView
from ticket.views import TicketDetailsView, UserTicketListView


urlpatterns = [
    path('', UserTicketListView.as_view(), name='Tickets-all'),
    path('detail/<int:pk>', TicketDetailsView.as_view(), name='Ticket-detail'),
]