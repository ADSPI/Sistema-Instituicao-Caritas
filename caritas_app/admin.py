from django.contrib import admin
from caritas_app import models


# Register your models here.

admin.site.register(models.Responsavel)
admin.site.register(models.Instrutor)
admin.site.register(models.Atendido)
admin.site.register(models.Oficina)
admin.site.register(models.Espaco)
admin.site.register(models.Periodo)
admin.site.register(models.Atividade)
admin.site.register(models.Turma)
admin.site.register(models.Responsavel_Atividade)
admin.site.register(models.Periodo_Atividade)
admin.site.register(models.Espaco_Atividade)
admin.site.register(models.Turma_Atendido)
admin.site.register(models.Chamada)
admin.site.register(models.Turma_Atendido_Chamada)
