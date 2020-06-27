from django import forms
from caritas_app import models


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = models.Responsavel
        fields = (
            'nome_responsavel',
            'rg_responsavel',
            'nis_responsavel',
            'cpf_responsavel',
            'nascimento_responsavel',
            'rua_responsavel',
            'numero_responsavel',
            'bairro_responsavel',
            'telefone_responsavel',
            'email_responsavel')

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = models.Instrutor
        fields = (
            'nome_instrutor',
            'especialidade_instrutor',
            'rg_instrutor',
            'cpf_instrutor',
            'nascimento_instrutor',
            'rua_instrutor',
            'numero_instrutor',
            'bairro_instrutor',
            'cidade_instrutor',
            'telefone_instrutor',
            'email_instrutor')

class AtendidoForm(forms.ModelForm):
    class Meta:
        model = models.Atendido
        fields = (
            'nome_atendido',
            'ra_atendido',
            'nis_atendido',
            'nascimento_atendido',
            'rua_atendido',
            'numero_atendido',
            'bairro_atendido',
            'cidade_atendido',
            'telefone_atendido',
            'email_atendido',
            'cod_responsavel'
        )

    def __init__(self, *args, **kwargs):
        super(AtendidoForm, self).__init__(*args, **kwargs)

class OficinaForm(forms.ModelForm):
    class Meta:
        model = models.Oficina
        fields = (
            'nome_oficina',
            'descricao_oficina',
            'objetivo_oficina',
            'publico_oficina'
        )

class EspacoForm(forms.ModelForm):
    class Meta:
        model = models.Espaco
        fields = (
            'nome_espaco',
            'lugares_espaco'
        )

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = models.Periodo
        fields = (
            'dia_periodo',
            'periodo_periodo',
            'horario_periodo'
        )

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = models.Atividade
        fields = (
            'cod_instrutor',
            'cod_oficina'
        )

class TurmaForm(forms.ModelForm):
    class Meta:
        model = models.Turma
        fields = (
            'nome_turma',
            'cod_atividade'
        )

class Responsavel_AtividadeForm(forms.ModelForm):
    class Meta:
        model = models.Responsavel_Atividade
        fields = (
            'cod_responsavel',
            'cod_atividade'
        )

class Periodo_AtividadeForm(forms.ModelForm):
    class Meta:
        model = models.Periodo_Atividade
        fields = (
            'cod_periodo',
            'cod_atividade'
        )

class Espaco_AtividadeForm(forms.ModelForm):
    class Meta:
        model = models.Espaco_Atividade
        fields = (
            'cod_espaco',
            'cod_atividade'
        )

class Turma_AtendidoForm(forms.ModelForm):
    class Meta:
        model = models.Turma_Atendido
        fields = (
            'cod_atendido',
            'cod_turma'
        )

class ChamadaForm(forms.ModelForm):
    class Meta:
        model = models.Chamada
        fields = (
            'data_chamada',
            'cod_turma',
            'atendidos_presentes'
        )

class Turma_Atendido_ChamadaForm(forms.ModelForm):
    class Meta:
        model = models.Turma_Atendido_Chamada
        fields = (
            'cod_turma_atendido',
            'cod_chamada',
            'presente_turma_atendido_chamada'
        )

