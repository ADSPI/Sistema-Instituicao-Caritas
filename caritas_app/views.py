from django.shortcuts import render, redirect
from django.http import HttpResponse
# impedir o acesso sem o login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import caritas_app.models
from caritas_app import forms
from django.db.models import OuterRef, Subquery
from datetime import datetime
#import caritas_app.forms

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')  # render(request, 'index.html')
        else:
            messages.error(request, "Usuáio ou senha incorreto")
    return redirect('/')  # render(request, 'index.html')

@login_required(login_url='/login/')
def menu(request):
    data = {}
    data['usuario'] = 'Henrique'
    return render(request, 'menu.html')

tabela = caritas_app.models

# ----------- EXIBE -----------#
@login_required(login_url='/login/')
def lista_atendidos(request):
    atendido = tabela.Atendido.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa: #Caso exista uma pesquisa
        atendido = tabela.Atendido.objects.filter(nome_atendido__icontains=pesquisa)
    dados = {'atendidos': atendido}
    return render(request, 'atendido.html', dados)
# PAREI AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII - JA ARRUMEI O HTML - FALTA TESTAR
@login_required(login_url='/login/')
def lista_responsaveis(request):
    responsavel = tabela.Responsavel.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa: #Caso exista uma pesquisa
        responsavel = tabela.Responsavel.objects.filter(nome_responsavel__icontains=pesquisa)
    dados = {'responsaveis': responsavel}
    return render(request, 'responsavel.html', dados)

@login_required(login_url='/login/')
def lista_instrutores(request):
    instrutor = tabela.Instrutor.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        instrutor = tabela.Instrutor.objects.filter(nome_instrutor__icontains=pesquisa)
    dados = {'instrutores': instrutor}
    return render(request, 'instrutor.html', dados)

@login_required(login_url='/login/')
def lista_oficinas(request):
    oficina = tabela.Oficina.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        oficina = tabela.Oficina.objects.filter(nome_oficina__icontains=pesquisa)
    dados = {'oficinas': oficina}
    return render(request, 'oficina.html', dados)

@login_required(login_url='/login/')
def lista_espaco(request):
    espaco = tabela.Espaco.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        espaco = tabela.Espaco.objects.filter(nome_espaco__icontains=pesquisa)
    dados = {'espacos': espaco}
    return render(request, 'espaco.html', dados)

@login_required(login_url='/login/')
def lista_periodos(request):
    periodo = tabela.Periodo.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        periodo = tabela.Periodo.objects.filter(dia_periodo__icontains=pesquisa)
    dados = {'periodos': periodo}
    return render(request, 'periodo.html', dados)

@login_required(login_url='/login/')
def lista_atividades(request):
    atividade = tabela.Atividade.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        atividade = tabela.Atividade.objects.filter(cod_atividade__icontains=pesquisa)
    dados = {'atividades': atividade}
    return render(request, 'atividade.html', dados)

@login_required(login_url='/login/')
def lista_turmas(request):
    turma = tabela.Turma.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        turma = tabela.Turma.objects.filter(nome_turma__icontains=pesquisa)
    dados = {'turmas': turma}
    return render(request, 'turma.html', dados)

# ----------- UPDATE -----------#
@login_required(login_url='/login/')
def atendido_update(request, cod_atendido):
    atendido = tabela.Atendido.objects.get(pk=cod_atendido) # se nao funcionar mudar id por pk
    form = caritas_app.forms.AtendidoForm(request.POST or None, instance=atendido)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_atendido')

    data['form'] = form
    return render(request, 'registro_atendido.html', data)

@login_required(login_url='/login/')
def responsavel_update(request, cod_responsavel):
    responsavel = tabela.Responsavel.objects.get(pk=cod_responsavel)
    form = caritas_app.forms.ResponsavelForm(request.POST or None, instance=responsavel)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_responsavel')

    data['form'] = form
    return render(request, 'registro_responsavel.html', data)

@login_required(login_url='/login/')
def instrutor_update(request, cod_instrutor):
    instrutor = tabela.Instrutor.objects.get(pk=cod_instrutor) # se nao funcionar mudar id por pk
    form = caritas_app.forms.InstrutorForm(request.POST or None, instance=instrutor)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_instrutor')

    data['form'] = form
    return render(request, 'registro_instrutor.html', data)

@login_required(login_url='/login/')
def oficina_update(request, cod_oficina):
    oficina = tabela.Oficina.objects.get(pk=cod_oficina) # se nao funcionar mudar id por pk
    form = caritas_app.forms.OficinaForm(request.POST or None, instance=oficina)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_oficina')

    data['form'] = form
    return render(request, 'registro_oficina.html', data)

@login_required(login_url='/login/')
def espaco_update(request, cod_espaco):
    espaco = tabela.Espaco.objects.get(pk=cod_espaco) # se nao funcionar mudar id por pk
    form = caritas_app.forms.EspacoForm(request.POST or None, instance=espaco)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_espaco')

    data['form'] = form
    return render(request, 'registro_espaco.html', data)

@login_required(login_url='/login/')
def periodo_update(request, cod_periodo):
    periodo = tabela.Periodo.objects.get(pk=cod_periodo) # se nao funcionar mudar id por pk
    form = caritas_app.forms.PeriodoForm(request.POST or None, instance=periodo)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_periodo')

    data['form'] = form
    return render(request, 'registro_periodo.html', data)

@login_required(login_url='/login/')
def atividade_update(request, cod_atividade):
    atividade = tabela.Atividade.objects.get(pk=cod_atividade) # se nao funcionar mudar id por pk
    form = caritas_app.forms.AtividadeForm(request.POST or None, instance=atividade)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_atividade')

    data['form'] = form
    return render(request, 'registro_atividade.html', data)

@login_required(login_url='/login/')
def turma_update(request, cod_turma):
    turma = tabela.Turma.objects.get(pk=cod_turma) # se nao funcionar mudar id por pk
    form = caritas_app.forms.TurmaForm(request.POST or None, instance=turma)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_turma')

    data['form'] = form
    return render(request, 'registro_turma.html', data)

# ----------- DELETE -----------#
@login_required(login_url='/login/')
def delete_atendido(request, cod_atendido):
    delete_item = tabela.Atendido.objects.get(pk=cod_atendido)
    delete_item.delete()
    return redirect('url_atendido')

@login_required(login_url='/login/')
def delete_responsavel(request, cod_responsavel):
    delete_item = tabela.Responsavel.objects.get(pk=cod_responsavel)
    delete_item.delete()
    return redirect('url_responsavel')

@login_required(login_url='/login/')
def delete_instrutor(request, cod_instrutor):
    delete_item = tabela.Instrutor.objects.get(pk=cod_instrutor)
    delete_item.delete()
    return redirect('url_instrutor')

@login_required(login_url='/login/')
def delete_oficina(request, cod_oficina):
    delete_item = tabela.Oficina.objects.get(pk=cod_oficina)
    delete_item.delete()
    return redirect('url_oficina')

@login_required(login_url='/login/')
def delete_espaco(request, cod_espaco):
    delete_item = tabela.Espaco.objects.get(pk=cod_espaco)
    delete_item.delete()
    return redirect('url_espaco')

@login_required(login_url='/login/')
def delete_periodo(request, cod_periodo):
    delete_item = tabela.Periodo.objects.get(pk=cod_periodo)
    delete_item.delete()
    return redirect('url_periodo')

@login_required(login_url='/login/')
def delete_atividade(request, cod_atividade):
    delete_item = tabela.Atividade.objects.get(pk=cod_atividade)
    delete_item.delete()
    return redirect('url_atividade')

@login_required(login_url='/login/')
def delete_turma(request, cod_turma):
    delete_item = tabela.Turma.objects.get(pk=cod_turma)
    delete_item.delete()
    return redirect('url_turma')


# ----------- CADASTRA-----------#
@login_required(login_url='/login/')
def cadastro_atendido(request):
    form = caritas_app.forms.AtendidoForm(request.POST or None)
    data = {}
    
    if form.is_valid():
        form.save()
        return redirect('url_atendido')

    data['form'] = form
    return render(request, 'registro_atendido.html', data)

@login_required(login_url='/login/')
def cadastro_responsavel(request):
    form = caritas_app.forms.ResponsavelForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_responsavel')

    data['form'] = form
    return render(request, 'registro_responsavel.html', data)

@login_required(login_url='/login/')
def cadastro_instrutor(request):
    form = caritas_app.forms.InstrutorForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_instrutor')

    data['form'] = form
    return render(request, 'registro_instrutor.html', data)

@login_required(login_url='/login/')
def cadastro_oficina(request):
    form = caritas_app.forms.OficinaForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_oficina')

    data['form'] = form
    return render(request, 'registro_oficina.html', data)

@login_required(login_url='/login/')
def cadastro_espaco(request):
    form = caritas_app.forms.EspacoForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_espaco')

    data['form'] = form
    return render(request, 'registro_espaco.html', data)

@login_required(login_url='/login/')
def cadastro_periodo(request):
    form = caritas_app.forms.PeriodoForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_periodo')

    data['form'] = form
    return render(request, 'registro_periodo.html', data)

@login_required(login_url='/login/')
def cadastro_atividade(request):
    form = caritas_app.forms.AtividadeForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_atividade')

    data['form'] = form
    return render(request, 'registro_atividade.html', data)

@login_required(login_url='/login/')
def cadastro_turma(request):
    form = caritas_app.forms.TurmaForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_turma')

    data['form'] = form
    return render(request, 'registro_turma.html', data)


# -----------Matricula-----------#
@login_required(login_url='/login/')
def matricular(request):
    form = caritas_app.forms.Turma_AtendidoForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_matriculados')

    data['form'] = form
    return render(request, 'matricular.html', data)

@login_required(login_url='/login/')
def matriculas(request):
    matricula = tabela.Turma_Atendido.objects.all()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa: #Caso exista uma pesquisa
        matricula = tabela.Turma_Atendido.objects.filter(cod_turma=pesquisa)
    dados = {'matriculas': matricula}
    return render(request, 'matriculas.html', dados)

@login_required(login_url='/login/')
def matricula_update(request, cod_turma_atendido):
    matricula = tabela.Turma_Atendido.objects.get(pk=cod_turma_atendido)
    form = caritas_app.forms.Turma_AtendidoForm(request.POST or None, instance=matricula)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_matriculados')

    data['form'] = form
    return render(request, 'matricular.html', data)

@login_required(login_url='/login/')
def delete_matricula(request, cod_turma_atendido):
    delete_item = tabela.Turma_Atendido.objects.get(pk=cod_turma_atendido)
    delete_item.delete()
    return redirect('url_matriculados')

# -----------Chamada-----------#
@login_required(login_url='/login/')
def realizar_chamada(request):
    form = caritas_app.forms.ChamadaForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_chamadas')

    data['form'] = form
    return render(request, 'realizar_chamada.html', data)

@login_required(login_url='/login/')
def chamadas(request):
    chamada = tabela.Chamada.objects.all().order_by('data_chamada').reverse()
    pesquisa = request.GET.get('pesquisa')
    if pesquisa: #Caso exista uma pesquisa
        pesquisa = datetime.strptime(pesquisa, "%d/%m/%Y")
        chamada = tabela.Chamada.objects.filter(data_chamada=pesquisa).order_by('data_chamada').reverse()
    dados = {'chamadas': chamada}
    return render(request, 'chamadas.html', dados)

@login_required(login_url='/login/')
def chamada_update(request, cod_chamada):
    chamada = tabela.Chamada.objects.get(pk=cod_chamada)
    form = caritas_app.forms.ChamadaForm(request.POST or None, instance=chamada)
    data = {}
    if form.is_valid():
        form.save()
        return redirect('url_chamadas')

    data['form'] = form
    return render(request, 'realizar_chamada.html', data)

@login_required(login_url='/login/')
def delete_chamada(request, cod_chamada):
    delete_item = tabela.Chamada.objects.get(pk=cod_chamada)
    delete_item.delete()
    return redirect('url_chamadas')