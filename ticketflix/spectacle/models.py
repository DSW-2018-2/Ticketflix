from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class SpectacleManager(models.Manager):
    def get_related_object(self, spectacle):
        if not spectacle:
            return self
        else:
            if spectacle.spectacle_type == 'FILME':
                return spectacle.movie_set.first()
            elif spectacle.spectacle_type == 'SHOW':
                return spectacle.show_set.first()
            elif spectacle.spectacle_type == 'PECA':
                return spectacle.play_set.first()

    def get_parent_object(self, spectacle):
        if not spectacle:
            return self
        else:
            return Spectacle.objects.get(
                id=spectacle.spectacle_id
            )


class SpectacleComponent(models.Model):
    class Meta:
        abstract = True

    PREESTREIA = 'PREESTREIA'
    EMCARTAZ = 'EMCARTAZ'
    LANCAMENTO = 'LANCAMENTO'
    FORACARTAZ = 'FORACARTAZ'
    EMBREVE = 'EMBREVE'

    LIVRE = 'LIVRE'
    DEZANOS = '10ANOS'
    DOZEANOS = '12ANOS'
    QUATORZEANOS = '14ANOS'
    DEZESSEISANOS = '16ANOS'
    MAIORESDEDEZOITO = 'MAIORES18'

    FILME = 'FILME'
    SHOW = 'SHOW'
    PECA ='PECA'
    NA = 'NA'

    STATUS_CHOICES = (
        (PREESTREIA, 'Pré-Estréia'),
        (EMCARTAZ, 'Em Cartaz'),
        (LANCAMENTO, 'Lançamento'),
        (FORACARTAZ, 'Fora de Cartaz'),
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

    SPECTACLE_CHOICES = (
        (FILME, 'Filme'),
        (SHOW, 'Show'),
        (PECA, 'Peça Teatral'),
        (NA, 'N/A'),
    )

    name = models.CharField(
        verbose_name=_('Nome'),
        help_text=_('Nome da Espetáculo'),
        max_length=100,
        default="",
    )

    status = models.CharField(
        verbose_name=_('Status do Espetáculo'),
        help_text=_('Status do Espetáculo'),
        max_length=15,
        choices=STATUS_CHOICES,
        default=EMBREVE
    )

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
        help_text=_('Duração do Espetáculo em minutos'),
        default=0
    )

    classification = models.CharField(
        verbose_name=_('Classificação Indicativa'),
        help_text=_('Classificação Indicativa do Espetáculo'),
        max_length=20,
        choices=CLASSIFICATION_CHOICES,
        default=LIVRE
    )

    spectacle_type = models.CharField(
        verbose_name=_('Tipo do Espetáculo'),
        help_text=_('Tipo do Espetáculo'),
        max_length=15,
        choices=SPECTACLE_CHOICES,
        default=NA
    )

    objects = SpectacleManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('spectacle:spectacle-detail', kwargs={'id': self.id})


class Spectacle(SpectacleComponent):
    class Meta:
        verbose_name = _("Espetáculo")
        verbose_name_plural = _("Espetáculos")


class SpectacleDecorator(SpectacleComponent):
    class Meta:
        abstract = True

    spectacle = models.ForeignKey(
        Spectacle,
        on_delete=models.PROTECT
    )


class Movie(SpectacleDecorator):
    class Meta:
        verbose_name = _("Filme")
        verbose_name_plural = _("Filmes")

    ANIMACAO = 'ANIMACAO'
    ACAO = 'ACAO'
    BIOGRAFIA = 'BIOGRAFIA'
    COMEDIA = 'COMEDIA'
    DOCUMENTARIO = 'DOCUMENTARIO'
    DRAMA = 'DRAMA'
    FICCAO = 'FICCAO'
    MUSICAL = 'MUSICAL'
    ROMANCE = 'ROMANCE'
    SUSPENSE = 'SUSPENSE'
    TERROR = 'TERROR'
    NA = 'NA'

    MOVIE_GENDER_OPTIONS = (
        (ANIMACAO, 'Animação'),
        (ACAO, 'Ação'),
        (BIOGRAFIA, 'Biografia'),
        (COMEDIA, 'Comédia'),
        (DOCUMENTARIO, 'Documentário'),
        (DRAMA, 'Drama'),
        (FICCAO, 'Ficção Científica'),
        (MUSICAL, 'Musical'),
        (NA, 'N/A'),
        (ROMANCE, 'Romance'),
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

    def __str__(self):
        return self.spectacle.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        spectacle = Spectacle.objects.get(id=self.spectacle_id)
        self.name = spectacle.name
        self.status = spectacle.status
        if spectacle.poster:
            self.poster = spectacle.poster
        self.duration = spectacle.duration
        self.classification = spectacle.classification
        self.spectacle_type = spectacle.spectacle_type
        super(Movie, self).save()


class Play(SpectacleDecorator):
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

    def __str__(self):
        return self.spectacle.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        spectacle = Spectacle.objects.get(id=self.spectacle_id)
        self.name = spectacle.name
        self.status = spectacle.status
        if spectacle.poster:
            self.poster = spectacle.poster
        self.duration = spectacle.duration
        self.classification = spectacle.classification
        self.spectacle_type = spectacle.spectacle_type
        super(Play, self).save()


class Show(SpectacleDecorator):
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

    def __str__(self):
        show_name = self.spectacle.name
        show_band = self.band
        show_tour = self.tour

        return '{}: {} - {}'.format(
            show_name,
            show_band,
            show_tour
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        spectacle = Spectacle.objects.get(id=self.spectacle_id)
        self.name = spectacle.name
        self.status = spectacle.status
        if spectacle.poster:
            self.poster = spectacle.poster
        self.duration = spectacle.duration
        self.classification = spectacle.classification
        self.spectacle_type = spectacle.spectacle_type
        super(Show, self).save()
