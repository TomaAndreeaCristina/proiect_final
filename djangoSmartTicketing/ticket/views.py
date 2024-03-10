from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from ticket.forms import TicketForm
from ticket.models import TicketModel, UserTicketModel


# Create your views here.
class TicketListView(DetailView):
    template_name = 'ticket/detalii.html'
    model = TicketModel



class UserTicketListView(DetailView):
    template_name = 'ticket/detalii_ticket.html'
    model = UserTicketModel



class TicketDetailsView(DetailView):
    template_name = 'ticket/detalii.html'
    model = TicketModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel


# Create your views here.

class ServiciiListView(ListView):
    template_name = 'servicii/all.html'
    model = ServiciiModel


class ServiciiDetaislView(DetailView):
    template_name = 'servicii/detalii.html'
    model = ServiciiModel

class ServiciiUpdateView(UpdateView):
    template_name = 'servicii/create_update_form.html'
    form_class = ServiciiForm
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')


class ServiciiDeleteView(DeleteView):
    template_name = 'servicii/delete_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')
    success_message = 'Serviciu sters!!!'


class ServiciiCreateView(CreateView):
    form_class = ServiciiForm
    template_name = 'servicii/create_update_form.html'
    model = ServiciiModel
    success_url = reverse_lazy('serviciu-all')