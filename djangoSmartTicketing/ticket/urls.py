from django.urls import path
from servicii.views import  ServiciiDetaislView, ServiciiUpdateView,ServiciiCreateView,ServiciiDeleteView
from ticket.views import TicketListView, TicketDetailsView

urlpatterns = [
    path('', TicketListView.as_view(), name='Tickets-all'),
    path('detail/<int:pk>', TicketDetailsView.as_view(), name='Ticket-detail'),
]