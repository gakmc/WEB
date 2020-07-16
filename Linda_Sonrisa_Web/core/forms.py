from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reserva, Producto

# class ReservaForm(ModelForm):

#     class Meta:
#         model = Reserva
#         fields = ['usuario','fecha_reserva', 'hora_reserva', 'especialidad']
#         widgets = {
#         'fecha_reserva': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 
#         'placeholder':'Select a date', 'type':'date'}),
#         'hora_reserva': forms.TimeInput(format=('%H:%M'), attrs={'class':'form-control'}),
#     }


# class CustomUserForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']




# class ProductosForm(forms.ModelForm): 
#     class Meta: 
#         model = Producto
#         fields = ('nomproducto', 'SKU', 'marca','descripcion', 'vencimiento', 'preciocompra', 'precioventa', 'stock', 'stockcritico')
#         labels = {
#             'nomproducto' : 'Nombre Producto'
#         }