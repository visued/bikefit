from django import forms
from .models import PerfilAvaliador, PerfilAtleta

class PerfilAvaliadorForm(forms.ModelForm):
    class Meta:
        model = PerfilAvaliador
        fields = '__all__'
        exclude = ['create', 'update']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do avaliador.'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email, Ex: email@suedcorps.com.'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone, Ex: DDD 99999-9999.'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade, Ex: São Paulo - SP.'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço, Ex: Rua São João, 9999 - Centro.'}),
            'empresa': forms.TextInput(attrs={'placeholder': 'Empresa, Ex: Sued Corps.'}),
            'cpf_cnpj': forms.TextInput(attrs={'placeholder': 'CPF/CNPJ, Ex: 999.999.999-46 / 99.999.999/0001-99.'}),
        }

class PerfilAtletaForm(forms.ModelForm):
    class Meta:
        model = PerfilAtleta
        fields = '__all__'
        exclude = ['create', 'update']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do atleta.'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email, Ex: email@suedcorps.com.'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone, Ex: DDD 99999-9999.'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade, Ex: São Paulo - SP.'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço, Ex: Rua São João, 9999 - Centro.'}),
            'data_nascimento': forms.TextInput(attrs={'placeholder': 'Nascimento, Ex: 26/09/1991.'}),
            'cpf_cnpj': forms.TextInput(attrs={'placeholder': 'CPF/CNPJ, Ex: 999.999.999-46 / 99.999.999/0001-99.'}),
            'ano_ini_esporte': forms.TextInput(attrs={'placeholder': 'Ano inicio do esporte, Ex: 2017.'}),
            'modalidade_principal': forms.Select(attrs={'placeholder': 'Modalidade principal, Ex: Speed de Estrada.'}),
            'vezes_treina': forms.Select(attrs={'placeholder': 'Treinos por semana, Ex: 7.'}),
            'duracao_treino': forms.TextInput(attrs={'placeholder': 'Duração do treino, Ex: 3 hrs.'}),
            'horas_trein_semana': forms.TextInput(attrs={'placeholder': 'Horas de treino por semana, Ex: 10 hrs.'}),
            'horas_trein_cada_modalidae': forms.Textarea(attrs={'placeholder': 'Horas treino por modalidade, Ex: Speed de Estrada: 5 hrs.'}),
            'modalidade_frequente': forms.TextInput(attrs={'placeholder': 'Modalidade treino frequente, Ex: Speed de Estrada.'}),
            'duracao_treino_longo': forms.TextInput(attrs={'placeholder': 'Duração do treino longo, Ex: 5 hrs.'}),
            'profissao': forms.TextInput(attrs={'placeholder': 'Profissão, Ex: Encanador.'}),
            'competicoes_frequenta': forms.Textarea(attrs={'placeholder': 'Competições que frequenta, Ex: Speed X MTB.'}),
            'duracao_provas': forms.TextInput(attrs={'placeholder': 'Duração das provas, Ex: 5 hrs.'}),
            'tipo_de_relevo': forms.Select(attrs={'placeholder': 'Tipo relevo, Ex: Plano, pouco de subida ou muita subida.'}),
            'nivel_atleta': forms.Select(attrs={'placeholder': 'Nivel do atleta, Ex: iniciante.'}),
            'outros': forms.Textarea(attrs={'placeholder': 'Comentários adicionais.'}),
        }