from ast import USub
from django.contrib import admin
from animais.models import Resgate, Denuncia, Usuario, EmailUsuario, Cidade, Estado, Situacao

admin.site.register(Resgate)
admin.site.register(Denuncia)
admin.site.register(Usuario)
admin.site.register(EmailUsuario)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Situacao)

# Register your models here.
