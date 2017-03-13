from rest_framework import serializers
from cadastros.models import PerfilAtleta

class PerfilAtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilAtleta
        fields = ['nome', 'email', 'telefone', 'cidade', 'endereco', 'data_nascimento', 'cpf_cnpj',
                  'ano_ini_esporte', 'modalidade_principal', 'vezes_treina', 'duracao_treino', 'horas_trein_semana',
                  'rg', 'modalidade_frequente', 'duracao_treino_longo', 'profissao', 'competicoes_frequenta',
                  'duracao_provas', 'tipo_de_relevo', 'nivel_atleta', 'outros']