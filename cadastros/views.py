from django.shortcuts import render
from .forms import PerfilAvaliadorForm, PerfilAtletaForm
from django.views.generic import FormView, DetailView
from django.contrib import messages

from .models import PerfilAvaliador

class PerfilAvaliadorFormView(FormView):
    def get(self, request, *args, **kwargs):
        formAvaliador = PerfilAvaliadorForm()
        context = {
            'title': 'Novo Avaliador',
            'formAvaliador': formAvaliador
        }
        return render(request, 'cadastro-avaliador.html', context)


    def post(self, request, *args, **kwargs):
        formAvaliadorSalva = PerfilAvaliadorForm(request.POST)
        formAvaliadorSalva.save()
        formAvaliadorSalva = PerfilAvaliadorForm
        messages.success(request, 'Os dados foram cadastrados com sucesso.')

        context = {
            'title': 'Novo Avaliador',
            'formAvaliador': formAvaliadorSalva,
        }
        return render(request, 'cadastro-avaliador.html', context)

class PerfilAtletaFormView(FormView):
    def get(self, request, *args, **kwargs):
        formAtleta = PerfilAtletaForm()
        context = {
            'title': 'Novo Atleta',
            'formAtleta': formAtleta
        }
        return render(request, 'cadastro-atleta.html', context)


    def post(self, request, *args, **kwargs):
        formAtletaSalva = PerfilAtletaForm(request.POST)
        formAtletaSalva.save()
        formAtletaSalva = PerfilAtletaForm
        messages.success(request, 'Os dados foram cadastrados com sucesso.')

        context = {
            'title': 'Novo Avaliador',
            'formAtleta': formAtletaSalva,
        }
        return render(request, 'cadastro-atleta.html', context)

def listaAvaliadores(request):
    try:
        atletas = PerfilAvaliador.objects.all()
    except:
        PerfilAvaliador.DoesNotExist

    return render(request, 'lista-avaliadores.html', {'avaliadores': atletas})

class AvaliadorDetailView(DetailView):
    model = PerfilAvaliador
    template_name = 'lista.html'