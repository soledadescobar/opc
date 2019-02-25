# Register your models here.
from django.contrib import admin

from .models import Variablesmacroeconomicas
from .models import Diashabiles
from .models import Serieipc

admin.site.register(Variablesmacroeconomicas)
admin.site.register(Diashabiles)
admin.site.register(Serieipc)