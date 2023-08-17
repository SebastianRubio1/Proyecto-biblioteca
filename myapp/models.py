from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    name=models.CharField(max_length=50,help_text="Ingresa el nombre de la biblioteca.")
    direccion=models.CharField(max_length=100,help_text="Ingresa la dirección de la biblioteca")

class Libro(models.Model):
    biblioteca=models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,help_text="Ingrese el nombre del libro")
    isbn=models.CharField(max_length=100,help_text="Ingrese el número ISBN del libro")
    autor= models.CharField(max_length=50,help_text="Ingresa el autor del libro")
    done=models.BooleanField(max_length=8,help_text="Ingrese si el libro esta prestado o en sala")