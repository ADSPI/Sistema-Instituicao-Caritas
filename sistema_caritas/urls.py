"""sistema_caritas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from caritas_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/submit', views.submit_login),
    path('login/', views.login_user),
    path('logout/', views.logout_user, name='url_logout'),
    path('', RedirectView.as_view(url='/menu/')),
    path('menu/', views.menu, name='url_menu'),


    # ---------------------------Listar------------------------- #
    path('atendidos/', views.lista_atendidos, name='url_atendido'),
    path('responsaveis/', views.lista_responsaveis, name='url_responsavel'),
    path('instrutores/', views.lista_instrutores, name='url_instrutor'),
    path('oficinas', views.lista_oficinas, name='url_oficina'),
    path('espaco', views.lista_espaco, name='url_espaco'),
    path('periodo', views.lista_periodos, name='url_periodo'),
    path('atividades', views.lista_atividades, name='url_atividade'),
    path('turmas', views.lista_turmas, name='url_turma'),

    # --------------------------- Alterar ------------------------- #
    path('atendido_update/<int:cod_atendido>/', views.atendido_update, name='url_atendido_update'),
    path('responsavel_update/<int:cod_responsavel>/', views.responsavel_update, name='url_responsavel_update'),
    path('instrutor_update/<int:cod_instrutor>/', views.instrutor_update, name='url_instrutor_update'),
    path('oficina_update/<int:cod_oficina>/', views.oficina_update, name='url_oficina_update'),
    path('espaco_update/<int:cod_espaco>/', views.espaco_update, name='url_espaco_update'),
    path('periodo_update/<int:cod_periodo>/', views.periodo_update, name='url_periodo_update'),
    path('atividade_update/<int:cod_atividade>/', views.atividade_update, name='url_atividade_update'),
    path('turma_update/<int:cod_turma>/', views.turma_update, name='url_turma_update'),

    # ---------------------------Cadastrar ------------------------- #
    path('atendido/cadastrar/', views.cadastro_atendido, name='url_atendido_cadastro'),
    path('responsaveis/cadastrar/', views.cadastro_responsavel, name='url_responsavel_cadastro'),
    path('instrutor/cadastrar/', views.cadastro_instrutor, name='url_instrutor_cadastro'),
    path('oficinas/cadastrar/', views.cadastro_oficina, name='url_oficina_cadastro'),
    path('espaco/cadastrar/', views.cadastro_espaco, name='url_espaco_cadastro'),
    path('periodo/cadastrar/', views.cadastro_periodo, name='url_periodo_cadastro'),
    path('atividades/cadastrar/', views.cadastro_atividade, name='url_atividade_cadastro'),
    path('turmas/cadastrar/', views.cadastro_turma, name='url_turma_cadastro'),


    # ---------------------------Deletes------------------------- #
    path('atendidos/delete/<int:cod_atendido>/', views.delete_atendido, name='url_atendido_delete'),
    path('responsaveis/delete/<int:cod_responsavel>/', views.delete_responsavel, name='url_responsavel_delete'),
    path('instrutores/delete/<int:cod_instrutor>/', views.delete_instrutor, name='url_instrutor_delete'),
    path('oficinas/delete/<int:cod_oficina>/', views.delete_oficina, name='url_oficina_delete'),
    path('espaco/delete/<int:cod_espaco>/', views.delete_espaco, name='url_espaco_delete'),
    path('periodo/delete/<int:cod_periodo>/', views.delete_periodo, name='url_periodo_delete'),
    path('atividades/delete/<int:cod_atividade>/', views.delete_atividade, name='url_atividade_delete'),
    path('turmas/delete/<int:cod_turma>/', views.delete_turma, name='url_turma_delete'),

    # ---------------------------Matrícula------------------------- #
    path('matricular/', views.matricular, name='url_matricular'),
    path('matriculas/', views.matriculas, name='url_matriculados'),
    path('matricular/delete/<int:cod_turma_atendido>/', views.delete_matricula, name='url_matricula_delete'),
    path('matriculas/update/<int:cod_turma_atendido>/', views.matricula_update, name='url_matricula_update'),

    # ---------------------------Chamada------------------------- #
    path('chamadas/', views.chamadas, name='url_chamadas'),
    path('realizar_chamadas/', views.realizar_chamada, name='url_realizar_chamada'),
    path('chamada/delete/<int:cod_chamada>/', views.delete_chamada, name='url_chamada_delete'),
    path('chamada/update/<int:cod_chamada>/', views.chamada_update, name='url_chamada_update'),
]
