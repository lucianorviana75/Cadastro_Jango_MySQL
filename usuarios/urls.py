from django.urls import path
from . import views

urlpatterns = [
    # Usuários
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),

    # Serviços
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    path('servicos/adicionar/', views.adicionar_servico, name='adicionar_servico'),
    path('servicos/deletar/<int:servico_id>/', views.deletar_servico, name='deletar_servico'),
]
