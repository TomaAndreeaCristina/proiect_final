from ticket.forms import TicketForm
from ticket.models import TicketModel, UserTicketModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView


class CreateTicketView(CreateView):
    model = TicketModel
    form_class = TicketForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('Tickets-all')


class UserTicketListView(ListView):
    template_name = 'ticket/detalii_ticket.html'
    model = UserTicketModel


class TicketDetailsView(DetailView):
    template_name = 'ticket/detalii.html'
    model = TicketModel
