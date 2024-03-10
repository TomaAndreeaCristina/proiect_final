from django.db import models

# Create your models here.
class UserModel(models.Model):
    nume_user = models.CharField(max_length=50,null=False)
    prenume_user = models.CharField(max_length=50,null=False)
    email_user = models.EmailField(max_length=50,null=False)
    telefon = models.CharField(max_length=12,null=False)
    nume_societate = models.CharField(max_length=50,null=False)
    cui_societate = models.CharField(max_length=10,null=False)
    angajat = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.nume_user} - {self.prenume_user} - {self.nume_societate} - "