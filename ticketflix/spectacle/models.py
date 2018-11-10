from django.db import models
from django.utils.translation import ugettext_lazy as _


class SpectacleComponent(models.Model):
    class Meta:
        abstract = True

    PREESTREIA = 'PREESTREIA'
    EMCARTAZ = 'EMCARTAZ'
    LANCAMENTO = 'LANCAMENTO'
    FORACATAZ = 'FORACARTAZ'
    EMBREVE = 'EMBREVE'

    LIVRE = 'LIVRE'
    DEZANOS = '10ANOS'
    DOZEANOS = '12ANOS'
    QUATORZEANOS = '14ANOS'
    DEZESSEISANOS = '16ANOS'
    MAIORESDEDEZOITO = 'MAIORES18'

    STATUS_CHOICES = (
        (PREESTREIA, 'Pré-Estréia'),
        (EMCARTAZ, 'Em Cartaz'),
        (LANCAMENTO, 'Lançamento'),
        (FORACATAZ, 'Fora de Cartaz'),
        (EMBREVE, 'Em Breve'),
    )

    CLASSIFICATION_CHOICES = (
        (LIVRE, 'Livre'),
        (DEZANOS, '10 Anos'),
        (DOZEANOS, '12 Anos'),
        (QUATORZEANOS, '14 Anos'),
        (DEZESSEISANOS, '16 Anos'),
        (MAIORESDEDEZOITO, 'Maiores de 18 Anos'),
    )

    name = models.CharField(
        verbose_name=_('Nome'),
        help_text=_('Nome da Espetáculo'),
        max_length=100,
        default="",
    )

    # audience = models.PositiveIntegerField(
    #     _('Audiência'),
    #     help_text=_(''),
    #     default=0
    # )

    status = models.CharField(
        verbose_name=_('Status do Espetáculo'),
        help_text=_(''),
        max_length=15,
        choices=STATUS_CHOICES,
        default=EMBREVE
    )

    # session = models.ForeignKey()
    #
    # establishment = models.ForeignKey()

    poster = models.ImageField(
        upload_to='media/',
        help_text=_("Poster do Espetáculo"),
        verbose_name=_('Poster'),
        blank=True,
        null=True,
        max_length=500
    )

    duration = models.PositiveIntegerField(
        verbose_name=_('Duração'),
        help_text=_('Duração do Espetáculo'),
        default=0
    )

    classification = models.CharField(
        verbose_name=_('Classificação Indicativa'),
        help_text=_('Classificação Indicativa do Espetáculo'),
        max_length=20,
        choices=CLASSIFICATION_CHOICES,
        default=LIVRE
    )

    def __str__(self):
        return self.name


class Spectacle(SpectacleComponent):
    class Meta:
        verbose_name = _("Espetáculo")
        verbose_name_plural = _("Espetáculos")


class SpectacleDecorator(SpectacleComponent, models.Model):
    class Meta:
        abstract = True

    spectacle = SpectacleComponent

    def __init__(self, spectacle):
        super().__init__()
        self._spectacle = spectacle


class Movie(SpectacleDecorator, models.Model):
    class Meta:
        verbose_name = _("Filme")
        verbose_name_plural = _("Filmes")

    ANIMACAO = 'ANIMACAO'
    ACAO = 'ACAO'
    BIOGRAFIA = 'BIOGRAFIA'
    COMEDIA = 'COMEDIA'
    DOCMUNETARIO = 'DOCUMENTARIO'
    DRAMA = 'DRAMA'
    FICCAO = 'FICCAO'
    MUSICAL = 'MUSICAL'
    ROMAMANCE = 'ROMANCE'
    SUSPENSE = 'SUSPENSE'
    TERROR = 'TERROR'
    NA = 'NA'

    MOVIE_GENDER_OPTIONS = (
        (ANIMACAO, 'Animação'),
        (ACAO, 'Ação'),
        (BIOGRAFIA, 'Biografia'),
        (COMEDIA, 'Comédia'),
        (DOCMUNETARIO, 'Documentário'),
        (DRAMA, 'Drama'),
        (FICCAO, 'Ficção Científica'),
        (MUSICAL, 'Musical'),
        (NA, 'N/A'),
        (ROMAMANCE, 'Romance'),
        (SUSPENSE, 'Suspense'),
        (TERROR, 'Terror'),
    )

    synopsis = models.TextField(
        verbose_name=_('Sinopse'),
        help_text=_('Sinopse do Filme'),
        max_length=500,
        default=""
    )

    diretor = models.CharField(
        verbose_name=_('Diretor'),
        help_text=_('Diretor do Filme'),
        max_length=255,
        default=""
    )

    cast = models.TextField(
        verbose_name=_('Elenco'),
        help_text=_('Elenco participante do Filme'),
        max_length=500,
        default=""
    )

    producer = models.CharField(
        verbose_name=_('Produtor'),
        help_text=_('Produtor do Filme'),
        max_length=255,
        default=""
    )

    writer = models.CharField(
        verbose_name=_('Escritor'),
        help_text=_('Escritor do Filme'),
        max_length=255,
        default=""
    )

    gender = models.CharField(
        verbose_name=_('Genêro'),
        help_text=_('Genêro do Filme'),
        choices=MOVIE_GENDER_OPTIONS,
        max_length=20,
        default=NA
    )

    trailer = models.CharField(
        verbose_name=_('Trailer'),
        help_text=_('Link do Trailer do Filme'),
        max_length=255,
        default=""
    )

    spectacle = models.ForeignKey(
        SpectacleDecorator,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.spectacle.name


class Play(SpectacleDecorator, models.Model):
    class Meta:
        verbose_name = _("Peça Teatral")
        verbose_name_plural = _("Peças Teatrais")

    AUTO = 'AUTO'
    BURLESCO = 'BURLESCO'
    CIRCENSE = 'CIRCENSE'
    COMEDIA = 'COMEDIA'
    DRAMA = 'DRAMA'
    FARSA = 'FARSA'
    MIMICA = 'MIMICA'
    MUSICAL = 'MUSAICAL'
    OUTROS = 'OUTROS'
    TRAGEDIA = 'TRAGEDIA'
    TRAGICOMEDIA = 'TRAGICOMEDIA'

    PLAY_GENDER_OPTIONS = (
        (AUTO, 'Auto'),
        (BURLESCO, 'Burlesco'),
        (CIRCENSE, 'Circense'),
        (COMEDIA, 'Comédia'),
        (DRAMA, 'Drama'),
        (FARSA, 'Farsa'),
        (MIMICA, 'Mímica'),
        (MUSICAL, 'Musical'),
        (OUTROS, 'Outros'),
        (TRAGEDIA, 'Tragédia'),
        (TRAGICOMEDIA, 'Tragicomédia'),
    )

    synopsis = models.TextField(
        verbose_name=_('Sinopse'),
        help_text=_('Sinopse do Peça'),
        max_length=500,
        default=""
    )

    diretor = models.CharField(
        verbose_name=_('Diretor'),
        help_text=_('Diretor do Peça'),
        max_length=255,
        default=""
    )

    cast = models.TextField(
        verbose_name=_('Elenco'),
        help_text=_('Elenco participante do Peça'),
        max_length=500,
        default=""
    )

    writer = models.CharField(
        verbose_name=_('Escritor'),
        help_text=_('Escritor do Peça'),
        max_length=255,
        default=""
    )

    producer = models.CharField(
        verbose_name=_('Produtor'),
        help_text=_('Produtor do Peça'),
        max_length=255,
        default=""
    )

    gender = models.CharField(
        verbose_name=_('Genêro'),
        help_text=_('Genêro do Peça'),
        choices=PLAY_GENDER_OPTIONS,
        max_length=15,
        default=OUTROS
    )

    spectacle = models.ForeignKey(
        SpectacleDecorator,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.spectacle.name


class Show(SpectacleDecorator, models.Model):
    class Meta:
        verbose_name = _("Show")
        verbose_name_plural = _("Shows")

    band = models.CharField(
        verbose_name=_('Banda/Artista'),
        help_text=_('Nome da(o) Banda/Artista'),
        max_length=255,
        default=""
    )

    tour = models.CharField(
        verbose_name=_('Turnê'),
        help_text=_('Nome da Turnê'),
        max_length=255,
        default=""
    )

    description = models.TextField(
        verbose_name=_('Descrição do Show'),
        help_text=_('Descrição do Show'),
        max_length=500,
        default=""
    )

    spectacle = models.ForeignKey(
        SpectacleDecorator,
        on_delete=models.CASCADE
    )

    def __str__(self):
        spetacle_name = self.spetacle.name
        band_name = self.band
        tour_name = self.tour
        show_name = "{} - {} - {}".format(
            spetacle_name,
            band_name,
            tour_name
        )

        return show_name
