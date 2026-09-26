from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Uses email as the primary identifier instead of username for authentication.
    Incorporates role-based flags for marketplace access control.
    """
    email = models.EmailField(
        unique=True,
        verbose_name='Correo Electrónico',
        help_text='Correo Electrónico único utilizado como identificador de acceso.'
    )
    is_merchant = models.BooleanField(
        default=False,
        verbose_name='Es Vendedor',
        help_text='Permite publicar productos y gestionar inventario en el marketplace.'
    )
    is_customer = models.BooleanField(
        default=True,
        verbose_name='Es Comprador',
        help_text='Permite realizar compras, añadir al carrito y gestionar pedidos.'
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Número de Teléfono'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'nexus_users'

    def __str__(self):
        return f"{self.email} ({self.username})"