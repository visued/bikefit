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


NIVEL_FLEXIBILIDADE_QUADRIL = (
    ('Muito Baixo', 'Muito Baixo'),
    ('Baixo', 'Baixo'),
    ('Moderado', 'Moderado'),
    ('Grande', 'Grande'),
    ('Muito Grande', 'Muito Grande'),
)

NIVEL_FLEXIBILIDADE_JOELHO = (
    ('Muito Baixo', 'Muito Baixo'),
    ('Baixo', 'Baixo'),
    ('Moderado', 'Moderado'),
    ('Grande', 'Grande'),
    ('Muito Grande', 'Muito Grande'),
)

NIVEL_FLEXIBILIDADE_OMBRO = (
    ('Muito Baixo', 'Muito Baixo'),
    ('Baixo', 'Baixo'),
    ('Moderado', 'Moderado'),
    ('Grande', 'Grande'),
    ('Muito Grande', 'Muito Grande'),
)

ESCOLIOSE = (
    ('Forte', 'Forte'),
    ('Leve', 'Leve'),
    ('Neutra', 'Neutra'),
)

LOMBARES = (
    ('Lordose', 'Lordose'),
    ('Muito Aumentada', 'Muita Aumentada'),
    ('Pouco Aumentada', 'Pouco Aumentada'),
    ('Neutral', 'Neutral'),
    ('Retificada', 'Retificada'),
)

CERVICAIS = (
    ('Muito Aumentada', 'Muita Aumentada'),
    ('Pouco Aumentada', 'Pouco Aumentada'),
    ('Neutral', 'Neutral'),
    ('Retificada', 'Retificada'),
)

JOELHO_LAT = (
    ('Muito Valgo', 'Muito Valgo'),
    ('Valgo', 'Valgo'),
    ('Muito Varo', 'Muito Varo'),
    ('Varo', 'Varo'),
)

JOELHO_ANT = (
    ('Encurtado', 'Encurtado'),
    ('Normal', 'Normal'),
    ('Hiperextenção','Hiperextenção')
)

PE = (
    ('Muito Pronado', 'Muito Pronado'),
    ('Pronado', 'Pronado'),
    ('Neutro', 'Neutro'),
    ('Supinado', 'Supinado'),
    ('Muito Supinado', 'Muito Supinado'),
)

OMBRO = (
    ('Muito Aduzido', 'Muito Aduzido'),
    ('Pouco Aduzido', 'Pouco Aduzido'),
    ('Neutron', 'Neutron'),
    ('Pouco Retraido', 'Pouco Retraido'),
    ('Muito Retraido', 'Muito Retraido'),
)

COTOVELO = (
    ('Hiperextenção Grande', 'Hiperextenção Grande'),
    ('Hiperextenção Pequena', 'Hiperextenção Pequena'),
    ('Neutron', 'Neutron'),
    ('Pouco Retraido', 'Pouco Retraido'),
    ('Muito Retraido', 'Muito Retraido'),
)

class AvaliacaoPostural(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    atleta = models.ForeignKey("PerfilAtleta")
    ###esqueleto 1 - lesões
    jl_L_Shoulder_tend = models.CharField('Ombro Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Shoulder_tend = models.CharField('Ombro Direito', max_length=255, null=True, blank=True)
    jl_L_Elbow_tend = models.CharField('Cotovelo Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Elbow_tend = models.CharField('Cotovelo Direito',max_length=255, null=True, blank=True)
    jl_L_Wrist_tend = models.CharField('Mão Esquerda',max_length=255, null=True, blank=True)
    jl_R_Wrist_tend = models.CharField('Mão Direita',max_length=255, null=True, blank=True)
    jl_C_Spine_tend = models.CharField('Coluna Cervical',max_length=255, null=True, blank=True)
    jl_T_Spine_tend = models.CharField('Coluna Torácica',max_length=255, null=True, blank=True)
    jl_L_Spine_tend = models.CharField('Coluna Lombar',max_length=255, null=True, blank=True)
    jl_L_Hip_tend = models.CharField('Quadril Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Hip_tend = models.CharField('Quadril Direito', max_length=255, null=True, blank=True)
    jl_L_Knee_tend = models.CharField('Joelho Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Knee_tend = models.CharField('Joelho Direito',max_length=255, null=True, blank=True)
    jl_L_Ankle_tend = models.CharField('Pé Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Ankle_tend = models.CharField('Pé Direito',max_length=255, null=True, blank=True)
    jl_L_Shoulder_swol = models.NullBooleanField('OE',blank=True)
    jl_R_Shoulder_swol = models.NullBooleanField('OD',blank=True)
    jl_L_Elbow_swol = models.NullBooleanField('CE',blank=True)
    jl_R_Elbow_swol = models.NullBooleanField('CD',blank=True)
    jl_L_Wrist_swol = models.NullBooleanField('ME',blank=True)
    jl_R_Wrist_swol = models.NullBooleanField('MD',blank=True)
    jl_C_Spine_swol = models.NullBooleanField('CC',blank=True)
    jl_T_Spine_swol = models.NullBooleanField('CT',blank=True)
    jl_L_Spine_swol = models.NullBooleanField('CL',blank=True)
    jl_L_Hip_swol = models.NullBooleanField('QE',blank=True)
    jl_R_Hip_swol = models.NullBooleanField('QD', blank=True)
    jl_L_Knee_swol = models.NullBooleanField('JE',blank=True)
    jl_R_Knee_swol = models.NullBooleanField('JD',blank=True)
    jl_L_Ankle_swol = models.NullBooleanField('PE',blank=True)
    jl_R_Ankle_swol = models.NullBooleanField('PD',blank=True)

    ###esqueleto 2 - dores
    jl_L_Shoulder_tend2 = models.CharField('Ombro Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Shoulder_tend2 = models.CharField('Ombro Direito', max_length=255, null=True, blank=True)
    jl_L_Elbow_tend2 = models.CharField('Cotovelo Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Elbow_tend2 = models.CharField('Cotovelo Direito',max_length=255, null=True, blank=True)
    jl_L_Wrist_tend2 = models.CharField('Mão Esquerda',max_length=255, null=True, blank=True)
    jl_R_Wrist_tend2 = models.CharField('Mão Direita',max_length=255, null=True, blank=True)
    jl_C_Spine_tend2 = models.CharField('Coluna Cervical',max_length=255, null=True, blank=True)
    jl_T_Spine_tend2 = models.CharField('Coluna Torácica',max_length=255, null=True, blank=True)
    jl_L_Spine_tend2 = models.CharField('Coluna Lombar',max_length=255, null=True, blank=True)
    jl_L_Hip_tend2 = models.CharField('Quadril Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Hip_tend2 = models.CharField('Quadril Direito', max_length=255, null=True, blank=True)
    jl_L_Knee_tend2 = models.CharField('Joelho Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Knee_tend2 = models.CharField('Joelho Direito',max_length=255, null=True, blank=True)
    jl_L_Ankle_tend2 = models.CharField('Pé Esquerdo',max_length=255, null=True, blank=True)
    jl_R_Ankle_tend2 = models.CharField('Pé Direito',max_length=255, null=True, blank=True)
    jl_L_Shoulder_swol2 = models.NullBooleanField('OE',blank=True)
    jl_R_Shoulder_swol2 = models.NullBooleanField('OD',blank=True)
    jl_L_Elbow_swol2 = models.NullBooleanField('CE',blank=True)
    jl_R_Elbow_swol2 = models.NullBooleanField('CD',blank=True)
    jl_L_Wrist_swol2 = models.NullBooleanField('ME',blank=True)
    jl_R_Wrist_swol2 = models.NullBooleanField('MD',blank=True)
    jl_C_Spine_swol2 = models.NullBooleanField('CC',blank=True)
    jl_T_Spine_swol2 = models.NullBooleanField('CT',blank=True)
    jl_L_Spine_swol2 = models.NullBooleanField('CL',blank=True)
    jl_L_Hip_swol2 = models.NullBooleanField('QE',blank=True)
    jl_R_Hip_swol2 = models.NullBooleanField('QD', blank=True)
    jl_L_Knee_swol2 = models.NullBooleanField('JE',blank=True)
    jl_R_Knee_swol2 = models.NullBooleanField('JD',blank=True)
    jl_L_Ankle_swol2 = models.NullBooleanField('PE',blank=True)
    jl_R_Ankle_swol2 = models.NullBooleanField('PD',blank=True)

    nivel_flexibilidade_quadril =  models.CharField('Nível de Flexibilidade Quadril', max_length=25, choices=NIVEL_FLEXIBILIDADE_QUADRIL, null=True, blank=True)
    nivel_flexibilidade_joelho = models.CharField('Nível de Flexibilidade Joelho', max_length=25, choices=NIVEL_FLEXIBILIDADE_JOELHO, null=True, blank=True)
    nivel_flexibilidade_ombro = models.CharField('Nível de Flexibilidade Ombro', max_length=25, choices=NIVEL_FLEXIBILIDADE_OMBRO, null=True, blank=True)

    escoliose = models.CharField('Escoliose', max_length=25, choices=ESCOLIOSE, null=True, blank=True)
    escoliose_comen = models.CharField('Escoliose', max_length=255, null=True, blank=True)
    lombares = models.CharField('Lombares', max_length=25, choices=LOMBARES, null=True, blank=True)
    cervicais = models.CharField('Cervicais', max_length=255, null=True, blank=True)
    cifose = models.CharField('Cifose', max_length=25, choices=CERVICAIS, null=True, blank=True)
    mobilidade_quadril = models.CharField('Mobilidade de Quadril', max_length=255, null=True, blank=True)
    joelho_desvio_lat = models.CharField('Joelho Desvio Lateral', max_length=255, choices=JOELHO_LAT, null=True, blank=True)
    joelho_desvio_ant = models.CharField('Joelho Desvio Anteroposterior', max_length=255, choices=JOELHO_ANT, null=True, blank=True)
    pe = models.CharField('Pé', choices=PE, max_length=255, null=True, blank=True)
    ombro = models.CharField('Ombro', max_length=255, choices=OMBRO, null=True, blank=True)
    cotovelo = models.CharField('Cotovelo', max_length=255, choices=COTOVELO, null=True, blank=True)
    maos = models.CharField('Mãos', max_length=255, null=True, blank=True)
    assimetria_pernas = models.CharField('Assimetria Pernas', max_length=255, null=True, blank=True)
    assimetrias_braco = models.CharField('Assimetria Braços', max_length=255, null=True, blank=True)
    peS = models.IntegerField('Pé',null=True, blank=True)
    tibia = models.IntegerField('Tibia', null=True, blank=True)
    femur = models.IntegerField('Fêmur', null=True, blank=True)
    tronco = models.IntegerField('Tronco', null=True, blank=True)
    umero = models.IntegerField('Umero', null=True, blank=True)
    radio = models.IntegerField('Radio', null=True, blank=True)
    quadril = models.IntegerField('Quadril', null=True, blank=True)
    ombroS = models.IntegerField('Ombro', null=True, blank=True)
    cabeca = models.IntegerField('Cabeça', null=True, blank=True)

    ####medidas
    isquios = models.IntegerField('Isquios', null=True, blank=True)
    peM = models.IntegerField('Pé', null=True, blank=True)
    ombroM = models.IntegerField('Ombro', null=True, blank=True)
    bracosM = models.IntegerField('Braços', null=True, blank=True)
    cavalM = models.IntegerField('Cavalo', null=True, blank=True)
    troncoCava = models.IntegerField('Tronco + Cavalo', null=True, blank=True)
    altura = models.IntegerField('Altura', null=True, blank=True)

    ##medias bike
    larguraselim = models.CharField('Largura de Selim', max_length=255, null=True, blank=True)
    tamanhobike = models.CharField('Tamanho bike', max_length=255, null=True, blank=True)
    formatoguidao = models.CharField('Formato do guidão', max_length=255, null=True, blank=True)
    tamanhopevela = models.CharField('Tamanho do pé de vela', max_length=255, null=True, blank=True)
    comentariosgerais = models.CharField('Comentários Gerais', max_length=255, null=True, blank=True)