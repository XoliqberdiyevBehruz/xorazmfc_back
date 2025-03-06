import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

MAN, WOMEN, U19, U21 = ('Erkak', 'Ayol', 'U19', 'U21')
ACADEMY_COACH, TEAM_COACH = ('akademik murabbiy', 'jamoa murabbiy')

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class NewsCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("yangilik turi")
        verbose_name_plural = _('yangilik turlari')


class News(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("yangiliklar")
        verbose_name_plural = _('yangiliklar')


class PlayerCountry(BaseModel):
    flag = models.ImageField(upload_to='flags/%Y/%m/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("futbolchi mamlakati")
        verbose_name_plural = _('futbolchi mamlakatlari')


class PlayerPosition(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("futbolchi pozisiyasi")
        verbose_name_plural = _('futbolchi pozisiyalari')


class Players(BaseModel):
    GENDER = (
        (WOMEN, _("Ayol")),
        (MAN, _("Erkak")),
        (U19, _("U19")),
        (U21, _("U21")),
    )

    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='players/%Y/%m/')
    number = models.PositiveIntegerField()
    goal = models.IntegerField()
    match = models.IntegerField()
    assist = models.IntegerField()
    birth_date = models.DateField()
    height = models.CharField(max_length=255)
    country = models.ForeignKey(PlayerCountry, on_delete=models.CASCADE, related_name='players')
    gender = models.CharField(max_length=255, choices=GENDER)
    position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("futbolchi")
        verbose_name_plural = _('futbolchilar')
        ordering = ['-created_at']


class Partners(BaseModel):
    image = models.ImageField(upload_to='partners/%Y/%m/')
    link = models.URLField()

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = _("hamkor")
        verbose_name_plural = _('hamkorlar')

    
class AboutCompany(BaseModel):
    image = models.ImageField(upload_to='about_company/%Y/%m/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description[:20]
    
    class Meta:
        verbose_name = _("Klub haqida")
        verbose_name_plural = _('klub haqida')

    
class Stadium(BaseModel):
    image = models.ImageField(upload_to='stadiums/%Y/%m/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description[:20]
    
    class Meta:
        verbose_name = _("stadion haqida")
        verbose_name_plural = _('stadionlar haqida')


class Banner(BaseModel):
    banner = models.ImageField(upload_to='banners/%Y/%m/')
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("banner")
        verbose_name_plural = _('bannerlar')

    
class AboutAcademy(BaseModel):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_academy/%Y/%m/', null=True, blank=True)

    def __str__(self):
        return self.description[:20]
    
    class Meta:
        verbose_name = _("akademiya haqida")
        verbose_name_plural = _('akademiya haqida')


class CoachPosition(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("murabbiy pozitsiyasi")
        verbose_name_plural = _('murabbiy pozitsiyalari')


class Coach(BaseModel):
    GENDER = (
        (WOMEN, _("Ayol")),
        (MAN, _("Erkak")),
    )
    TYPE = (
        (ACADEMY_COACH, _('Akademik murabbiy')),
        (TEAM_COACH, _('Jamoa murabbiy')),
    )

    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='coaches/%Y/%m/')
    banner = models.ImageField(upload_to='coaches_banners/%Y/%m/', null=True, blank=True)
    position = models.ForeignKey(CoachPosition, on_delete=models.CASCADE, related_name='coaches')
    gender = models.CharField(max_length=255, choices=GENDER)     
    coach_type = models.CharField(max_length=255, choices=TYPE, default=TEAM_COACH)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("murabbiylar")
        verbose_name_plural = _('murabbiylar')


class CoachInformation(BaseModel):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='informations')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.coach} - {self.name}"
    
    class Meta:
        verbose_name = _("murabbiy malumoti")
        verbose_name_plural = _('murabbiy malumotlari')


class Leaders(BaseModel):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    image = models.ImageField(upload_to='leaders/%Y/%m/')
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("raxbariyat")
        verbose_name_plural = _('raxbariyat')