from django.db import models

class PerfilAvaliador(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    empresa = models.CharField(max_length=255)
    cpf_cnpj = models.CharField('CPF/CNPJ',max_length=12)

    def __str__(self):
        return self.nome



NIVEL_ATLETA = (
    ('', '--- Nível do atleta ---'),
    ('AM', 'Amador'),
    ('AMF', 'Amador Forte'),
    ('ALR', 'Alto Rendimento'),
    ('ALRP', 'Alto Rendimento Profissional'),
    ('RE', 'Recreacional'),
)

MODALIDADE_PRINCIPAL = (
    ('MP', '--- Modalide principal ---'),
    ('MT', 'MTB'),
    ('CICL', 'Ciclismo'),
    ('TRIL', 'Triathlon'),
    ('OU', 'Outros'),
)

VEZES_TREINO_SEMAN = (
    ('TR', '--- Treinos por semana ---'),
    ('UM', '1'),
    ('DOIS', '2'),
    ('TRES', '3'),
    ('QUATRO', '4'),
    ('CINCO', '5'),
    ('SEIS', '6'),
    ('SETE', '7'),
)

TIPO_RELEVO = (
    ('TO', '--- Tipo relevo ---'),
    ('PL', 'Plano'),
    ('PS', 'Pouco de subidas'),
    ('MS', 'Muitas subidas'),
)

class PerfilAtleta(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=8)
    cpf_cnpj = models.CharField('CPF/CNPJ',max_length=12)
    ano_ini_esporte = models.CharField(max_length=12)
    modalidade_principal = models.CharField(max_length=50, choices=MODALIDADE_PRINCIPAL)
    vezes_treina = models.CharField(max_length=50, choices=VEZES_TREINO_SEMAN)
    duracao_treino = models.CharField(max_length=50)
    horas_trein_semana = models.CharField(max_length=50)
    horas_trein_cada_modalidae = models.CharField(max_length=50)
    modalidade_frequente = models.CharField(max_length=50)
    duracao_treino_longo = models.CharField(max_length=50)
    profissao = models.CharField(max_length=50)
    competicoes_frequenta = models.CharField(max_length=50)
    duracao_provas = models.CharField(max_length=50)
    tipo_de_relevo = models.CharField(max_length=50, choices=TIPO_RELEVO)
    nivel_atleta = models.CharField(max_length=50, choices=NIVEL_ATLETA)
    outros = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
