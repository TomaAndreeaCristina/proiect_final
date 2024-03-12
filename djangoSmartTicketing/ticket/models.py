from django.db import models


# Create your models here.

class TicketModel(models.Model):
    nume_societate = models.CharField(max_length=50, null=False)
    nume_user = models.CharField(max_length=50, null=False)
    descriere_ticket = models.CharField(max_length=1000, null=False)
    status_ticket = models.CharField(max_length=50, null=False)

    # servicii = models.ForeignKey('ServiciiModel', on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.nume_user} a deschis ticket nr - {self.id}"


class UserTicketModel(models.Model):
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE)
    nume_user = models.CharField(max_length=50, null=False)
    data_inregistrare_user_ticket = models.CharField(max_length=50, null=False)
    data_inchidere_user_ticket = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return f"Tichetul nr {self.ticket.id} a fost deschis la ora- {self.data_inregistrare_user_ticket}"
