from django.db import models
from django.utils.translation import gettext_lazy as _

class classes(models.TextChoices):
    GUERREIRO = 'Guerreiro', _('Guerreiro')
    MAGO = 'Mago', _('Mago')
    ARQUEIRO = 'Arqueiro', _('Arqueiro')
    NECROMANTE = 'Necromante', _('Necromante')


class racas(models.TextChoices):
    HUMANO = 'Humano', _('Humano')
    ALTO_ELFO = 'Alto Elfo', _('Alto Elfo')
    ANAO = 'Anão', _('Anão')
    MEIO_DRAGAO = 'Meio Dragão', _('Meio Dragão')
    MEIO_ELFO = 'Meio Elfo', _('Meio Elfo')
    ESQUELETO = 'Esqueleto', _('Esqueleto')

class Destino(models.TextChoices):
    GLORIA =  'Glória', _('Glória eterna')
    VINGANCA = 'Vingança', _('Vingança sem fim')
    AMOR = 'Amor', _('Um belo amor')
