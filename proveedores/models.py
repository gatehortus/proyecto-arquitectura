from django.db import models
import uuid


class Proveedor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )    
    
    nombre = models.CharField(max_length=200)

    nit = models.CharField(
        max_length=50,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    telefono = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nombre
# Crea la clase proveedor según diagrama de clases
