from modeltranslation import translator

from common import models

@translator.register(models.NewsCategory)
class NewsCategoryTranslationOptions(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.News)
class NewsTranslationOptions(translator.TranslationOptions):
    fields = ('title', 'description')
    

@translator.register(models.PlayerPosition)
class PlayerPositionTranslationOptions(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.AboutCompany)
class AboutCompanyTranslationOptions(translator.TranslationOptions):
    fields = ('description',)

@translator.register(models.Stadium)
class StadiumTranslationOptions(translator.TranslationOptions):
    fields = ('description',)

@translator.register(models.Banner)
class BannerTranslationOptions(translator.TranslationOptions):
    fields = ('title',)

@translator.register(models.AboutAcademy)
class AboutAcademyTranslationOptions(translator.TranslationOptions):
    fields = ('description',)

@translator.register(models.CoachInformation)
class CoachInformationTranslationOptions(translator.TranslationOptions):
    fields = ('name', 'value')

@translator.register(models.CoachPosition)
class CoachPositionTranslationOptions(translator.TranslationOptions):
    fields = ('name',)