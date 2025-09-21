
from django.shortcuts import render



# Create your views here.
# crude usuarios
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Servico

# --------- Usuários ---------

def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Pega todos os usuários do banco
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        Usuario.objects.create(nome=nome, email=email)
        return redirect('listar_usuarios')
    return render(request, 'adicionar_usuario.html')

def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')


# --------- Serviços ---------

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'listar_servicos.html', {'servicos': servicos})

def adicionar_servico(request):
    if request.method == 'POST':
        nome_cliente = request.POST['nome_cliente']
        data_servico = request.POST['data_servico']  # formato YYYY-MM-DD
        tipo_servico = request.POST['tipo_servico']
        Servico.objects.create(nome_cliente=nome_cliente, data_servico=data_servico, tipo_servico=tipo_servico)
        return redirect('listar_servicos')
    return render(request, 'adicionar_servico.html')

def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    servico.delete()
    return redirect('listar_servicos')
