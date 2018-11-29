from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(
        max_length=80,
        null=False
    )

    descripcion = models.TextField(
        null=False
    )

    numero_usuarios = models.CharField(
        max_length=80,
        null=False
    )

    duracion = models.CharField(
        max_length=80,
        null=False
    )

    ubicacion = models.CharField(
        max_length=80,
        null=False
    )

    categoria = models.CharField(
        max_length=80,
        null=False
    )
