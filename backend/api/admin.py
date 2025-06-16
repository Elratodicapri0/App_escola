from django.contrib import admin
from api.models import Responsavel, Aluno, Professor, Bimestre, Nota, AtividadePendente, EventoExtracurricular, PagamentoPendente

class ResponsaveisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'adress', 'cpf', 'birthday')
    list_display_links = ('name', 'phone_number', 'email', 'adress')
    search_fields = ('name', 'cpf',)
    list_filter = ('name', 'cpf',)


class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_aluno', 'phone_number_aluno', 'email_aluno', 'cpf_aluno', 'birthday_aluno', 'faltas_aluno')
    list_display_links = ('name_aluno', 'phone_number_aluno', 'email_aluno', 'faltas_aluno')
    search_fields = ('name_aluno', 'cpf_aluno',)
    list_filter = ('name_aluno', 'cpf_aluno',)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_professor', 'phone_number_professor', 'email_professor', 'cpf_professor', 'birthday_professor', 'matricula_professor')
    list_display_links = ('name_professor', 'phone_number_professor', 'email_professor')
    search_fields = ('name_professor', 'cpf_professor',)
    list_filter = ('name_professor', 'cpf_professor',)


class BimestreAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero')
    list_filter = ('numero',)


class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'disciplina', 'bimestre', 'valor')
    list_filter = ('bimestre', 'disciplina', 'aluno')


class AtividadePendenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'disciplina', 'bimestre', 'descricao')
    list_filter = ('bimestre', 'disciplina', 'aluno')


class EventoExtracurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data', 'professor_id')
    search_fields = ('titulo', 'professor_id')
    list_filter = ('data',)


class PagamentoPendenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'valor', 'data_vencimento', 'descricao')
    search_fields = ('aluno__nome',)
    list_filter = ('data_vencimento',)

class ContratosAdmin(admin.ModelAdmin):
    list_display = ('id',  'complete_name_aluno', 'adress', 'cpf', 'birthday', 'complete_name','cpf_aluno', 'birthday_aluno')
    list_display_links = ( 'complete_name_aluno', 'adress', 'cpf', 'birthday', 'complete_name','cpf_aluno', 'birthday_aluno')
    list_filter = ('cpf', 'cpf_aluno')
    search_fields = ('cpf', 'cpf_aluno')


admin.site.register(Responsavel, ResponsaveisAdmin)
admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Bimestre, BimestreAdmin)
admin.site.register(AtividadePendente, AtividadePendenteAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(EventoExtracurricular, EventoExtracurricularAdmin)
admin.site.register(PagamentoPendente, PagamentoPendenteAdmin)

