from django import forms
from .models import PerfilAvaliador, PerfilAtleta, AvaliacaoPostural

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
            'email': forms.EmailInput(attrs={'placeholder': 'Email, Ex: email@suedcorps.com.'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone, Ex: DDD 99999-9999.'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade, Ex: São Paulo - SP.'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço, Ex: Rua São João, 9999 - Centro.'}),
            'data_nascimento': forms.DateInput(attrs={'placeholder': 'Nascimento, Ex: 1991-26-91'}, format='%d-%m-%Y'),
            'cpf_cnpj': forms.TextInput(attrs={'placeholder': 'CPF/CNPJ, Ex: 999.999.999-46 / 99.999.999/0001-99.'}),
            'rg': forms.NumberInput(),
            'ano_ini_esporte': forms.TextInput(attrs={'placeholder': 'Ano início do esporte, Ex: 2017.'}),
            'modalidade_principal': forms.Select(attrs={'placeholder': 'Modalidade principal, Ex: Speed de Estrada.'}),
            'vezes_treina': forms.NumberInput(attrs={'placeholder': 'Vezes que treina por semana.'}),
            'duracao_treino': forms.NumberInput(attrs={'placeholder': 'Duração média dos treinos'}),
            'horas_trein_semana': forms.NumberInput(attrs={'placeholder': 'Horas treino por semana.'}),
            'duracao_treino_longo': forms.TextInput(attrs={'placeholder': 'Duração do treino mais longo, Ex: 5 hrs.'}),
            'modalidade_frequente': forms.TextInput(attrs={'placeholder': 'Modalidade treino frequente, Ex: Speed de Estrada.'}),
            'profissao': forms.TextInput(attrs={'placeholder': 'Profissão, Ex: Encanador.'}),
            'competicoes_frequenta': forms.Textarea(attrs={'placeholder': 'Competições que frequenta, Ex: Speed X MTB.'}),
            'duracao_provas': forms.TextInput(attrs={'placeholder': 'Duração das provas, Ex: 5 hrs.'}),
            'tipo_de_relevo': forms.Select(attrs={'placeholder': 'Tipo relevo, Ex: Plano, pouco de subida ou muita subida.'}),
            'nivel_atleta': forms.Select(attrs={'placeholder': 'Nivel do atleta, Ex: iniciante.'}),
            'outros': forms.Textarea(attrs={'placeholder': 'Comentários adicionais.'}),
            # 'foto': forms.FileInput(attrs={'placeholder': 'Selecione suas fotos.'}),
        }

class AvaliacaoPosturalForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoPostural
        fields = '__all__'
        exclude = ['create', 'update']