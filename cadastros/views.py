from django.shortcuts import render, get_object_or_404
from .forms import PerfilAvaliadorForm, PerfilAtletaForm, AvaliacaoPosturalForm
from django.views.generic import FormView, DetailView
from django.contrib import messages

from .models import PerfilAvaliador, PerfilAtleta


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

class AvaliacaoPosturalFormView(FormView):
    def get(self, request, *args, **kwargs):
        formAvaliacaoPostural = AvaliacaoPosturalForm()
        context = {
            'title': 'Nova Avaliacao Postural',
            'formAvaliacaoPostural': formAvaliacaoPostural,
        }
        return render(request, 'avaliacao-postural.html', context)

    def post(self, request, *args, **kwargs):
        formAvaliacaoPosturalSalva = AvaliacaoPosturalForm(request.POST)
        formAvaliacaoPosturalSalva.save()
        formAvaliacaoPosturalSalva = AvaliacaoPosturalForm
        messages.sucess(request, 'Os dados foram salvos com sucesso.')

        context = {
            'title': 'Nova Avaliacao Postural',
            'formAvaliacaoPostural': formAvaliacaoPosturalSalva,
        }
        return render(request, 'avaliacao-postural.html', context)

    def atleta(self, request, pk):
        perfil = get_object_or_404(PerfilAtleta, pk=pk)
        context = {
            'perfil': perfil
        }
        return render(request, 'avaliacao-postural.html', context)


def listaAvaliadores(request):
    try:
        avaliadores = PerfilAvaliador.objects.all()
    except:
        PerfilAvaliador.DoesNotExist

    return render(request, 'lista-avaliadores.html', {'avaliadores': avaliadores})

def listaAtletas(request):
    try:
        atletas = PerfilAtleta.objects.all()
    except:
        PerfilAtleta.DoesNotExist

    return render(request, 'lista-atletas.html', {'atletas': atletas})


class AvaliadorDetailView(DetailView):
    model = PerfilAvaliador
    template_name = 'lista.html'

class AtletaDetailView(DetailView):
    model = PerfilAtleta
    template_name = 'detalhe-atleta.html'
