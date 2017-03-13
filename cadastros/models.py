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
    ('Amador', 'Amador'),
    ('Amador Forte', 'Amador Forte'),
    ('Alto Rendimento', 'Alto Rendimento'),
    ('Alto Rendimento Profissional', 'Alto Rendimento Profissional'),
    ('Recreacional', 'Recreacional'),
)

MODALIDADE_PRINCIPAL = (
    ('Mountain Bike', 'Mountain Bike'),
    ('Ciclismo de Estrada', 'Ciclismo de Estrada'),
    ('Triathlon', 'Triathlon'),
    ('Duathlon', 'Duathlon'),
    ('Outros', 'Outros'),
)

VEZES_TREINO_SEMAN = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
)

TIPO_RELEVO = (
    ('Plano', 'Plano'),
    ('Pouco de subidas', 'Pouco de subidas'),
    ('Muitas subidas', 'Muitas subidas'),
)

class PerfilAtleta(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email', max_length=30)
    telefone = models.IntegerField('Telefone', null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=50, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=50, null=True, blank=True)
    data_nascimento = models.DateField('Nascimento', null=True, blank=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14, null=True, blank=True)
    rg = models.IntegerField('RG', null=True, blank=True)
    ano_ini_esporte = models.IntegerField('Ano início do esporte', null=True, blank=True)
    modalidade_principal = models.CharField('Modalidade Principal', max_length=18, choices=MODALIDADE_PRINCIPAL, null=True, blank=True)
    vezes_treina = models.IntegerField('Vezes treino na semana', null=True, blank=True) #mudar para choices
    duracao_treino = models.IntegerField('Duração média dos treinos', null=True, blank=True) #mudar para choiices em meia em meira hora
    horas_trein_semana = models.IntegerField('Horas de treino na semana', null=True, blank=True)
    duracao_treino_longo = models.CharField('Duração do treino mais longo', max_length=50, null=True, blank=True)
    modalidade_frequente = models.CharField('Modalidade frequente', max_length=50, null=True, blank=True)
    profissao = models.CharField('Profissão', max_length=50, null=True, blank=True)
    competicoes_frequenta = models.CharField('Competições que frequenta', max_length=50, null=True, blank=True)
    duracao_provas = models.CharField('Duração das provas', max_length=50, null=True, blank=True)
    tipo_de_relevo = models.CharField('Tipo de relevo', max_length=50, choices=TIPO_RELEVO, null=True, blank=True)
    nivel_atleta = models.CharField('Nível do atleta', max_length=50, choices=NIVEL_ATLETA, null=True, blank=True)
    outros = models.CharField('Outros comentários', max_length=50, null=True, blank=True)
    # foto = models.ImageField('Fotos', null=True)

    def __str__(self):
        return self.nome

class AvaliacaoPostural(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    atleta = models.ForeignKey("PerfilAtleta")


