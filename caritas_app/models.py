from django.db import models

# Create your models here.

class Responsavel(models.Model):
    cod_responsavel = models.AutoField(primary_key=True, auto_created= True)
    nome_responsavel = models.CharField(max_length=50, null=False)
    rg_responsavel = models.CharField(max_length=9, null=False)
    nis_responsavel = models.CharField(max_length=11, null=False)
    cpf_responsavel = models.CharField(max_length=11, null=False)
    nascimento_responsavel = models.DateField(null=False)
    rua_responsavel = models.CharField(max_length=50, null=False)
    numero_responsavel = models.CharField(max_length=5, null=False)
    bairro_responsavel = models.CharField(max_length=30, null=False)
    telefone_responsavel = models.CharField(max_length=11, null=False)
    email_responsavel = models.EmailField()

    def __str__(self):
        return self.nome_responsavel

    class Meta:
        db_table = 'responsavel'

class Instrutor(models.Model):
    cod_instrutor = models.AutoField(auto_created=True, primary_key=True)
    nome_instrutor = models.CharField(max_length=50, null=False)
    especialidade_instrutor = models.CharField(max_length=9, null=False)
    rg_instrutor = models.CharField(max_length=9, null=False)
    cpf_instrutor = models.CharField(max_length=11, null=False)
    nascimento_instrutor = models.DateField(null=False)
    rua_instrutor = models.CharField(max_length=50, null=False)
    numero_instrutor = models.CharField(max_length=5, null=False)
    bairro_instrutor = models.CharField(max_length=30, null=False)
    cidade_instrutor = models.CharField(max_length=30, null=False)
    telefone_instrutor = models.CharField(max_length=11, null=False)
    email_instrutor = models.EmailField()   

    def __str__(self):
        return self.nome_instrutor
    
    class Meta:
        db_table = 'instrutor'

class Atendido(models.Model):
    cod_atendido = models.AutoField(auto_created=True, primary_key=True)
    nome_atendido = models.CharField(max_length=50, null=False)
    ra_atendido = models.CharField(max_length=20, null=False)
    nis_atendido = models.CharField(max_length=11, null=False)
    nascimento_atendido = models.DateField(null=False)
    rua_atendido = models.CharField(max_length=50, null=False)
    numero_atendido = models.CharField(max_length=5, null=False)
    bairro_atendido = models.CharField(max_length=30, null=False)
    cidade_atendido = models.CharField(max_length=30, null=False)
    telefone_atendido = models.CharField(max_length=11, null=False)
    email_atendido = models.EmailField(max_length=30)
    cod_responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'atendido'

    def __str__(self):
        return self.nome_atendido

class Oficina(models.Model):
    cod_oficina = models.AutoField(auto_created=True, primary_key=True)
    nome_oficina = models.CharField(max_length=50, null=False)
    descricao_oficina = models.CharField(max_length=500)
    objetivo_oficina = models.CharField(max_length=100)
    publico_oficina = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_oficina

    class Meta:
        db_table = 'oficina'

class Espaco(models.Model):
    cod_espaco = models.AutoField(auto_created=True, primary_key=True)
    nome_espaco = models.CharField(max_length=20, null=False)
    lugares_espaco = models.IntegerField(null=False)

    def __str__(self):
        return self.nome_espaco

    class Meta:
        db_table = 'espaco'

class Periodo(models.Model):
    cod_periodo = models.AutoField(auto_created=True, primary_key=True)
    dia_periodo = models.CharField(max_length=13, null=False)
    periodo_periodo = models.CharField(max_length=5, null=False)
    horario_periodo = models.TimeField(null=False)

    class Meta:
        db_table = 'periodo'

class Atividade(models.Model):
    cod_atividade = models.AutoField(auto_created=True, primary_key=True)
    cod_instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    cod_oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)

    class Meta:
        db_table = 'atividade'
        unique_together = (('cod_instrutor', 'cod_oficina'))

class Turma(models.Model):
    cod_turma = models.AutoField(auto_created=True, primary_key=True)
    nome_turma = models.CharField(max_length=15, null=False)
    cod_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_turma

    class Meta:
        db_table = 'turma'
        unique_together = (('cod_atividade', 'nome_turma'))


class Responsavel_Atividade(models.Model):
    cod_responsavel_atividade = models.AutoField(auto_created=True, primary_key=True)
    cod_responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    cod_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reponsavel_atividade'
        unique_together = (('cod_atividade', 'cod_responsavel'))

class Periodo_Atividade(models.Model):
    cod_periodo_atividade = models.AutoField(auto_created=True, primary_key=True)
    cod_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    cod_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('cod_periodo', 'cod_atividade'))
        db_table = 'periodo_atividade'

class Espaco_Atividade(models.Model):
    cod_espaco_atividade = models.AutoField(auto_created=True, primary_key=True)
    cod_espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    cod_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    class Meta:
        db_table = 'espaco_atividade'
        unique_together = (('cod_espaco', 'cod_atividade'))

class Turma_Atendido(models.Model):
    cod_turma_atendido = models.AutoField(auto_created=True, primary_key=True)
    cod_atendido = models.ForeignKey(Atendido, on_delete=models.CASCADE)
    cod_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


    class Meta:
        db_table = 'turma_atendido'
        unique_together = (('cod_atendido', 'cod_turma')) #cod_turma_atendido

class Chamada(models.Model):
    cod_chamada = models.AutoField(auto_created=True, primary_key=True)
    data_chamada = models.DateField(null=False)
    cod_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    atendidos_presentes = models.ManyToManyField(Atendido)

    def __str__(self):
        return str(self.data_chamada)
        
    class Meta:
        db_table = 'chamada'

class Turma_Atendido_Chamada(models.Model):
    cod_turma_atendido_chamada = models.AutoField(auto_created=True, primary_key=True)
    cod_turma_atendido = models.ForeignKey(Turma_Atendido, on_delete=models.CASCADE)
    cod_chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE)
    presente_turma_atendido_chamada = models.BooleanField(null=False)

    class Meta:
        db_table = 'turma_atendido_chamada'
        unique_together = (('cod_turma_atendido', 'cod_chamada')) #cod_turma_atendido

