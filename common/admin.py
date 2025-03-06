from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib.auth.models import User, Group

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from common import models

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(models.NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('name_uz', 'name_ru', 'name_en', 'news_count')
    list_display_links = list_display
    search_fields = ('name',)
    list_filter = ('created_at',)
    def news_count(self, obj):
        url = (
            reverse('admin:common_news_changelist') + '?'
            + urlencode({'category__id': obj.id})
        )
        return format_html('<a href="{}">{} news</a>', url, obj.news_count) 
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            news_count=Count('news')
        )
    

@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    prepopulated_fields = {
        'slug': ('title_uz',)
    }
    autocomplete_fields = ('category',)


@admin.register(models.PlayerCountry)
class PlayerCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'players_this_country', 'image')
    search_fields = ('name',)
    @admin.display(ordering='-players_this_country')
    def players_this_country(self, obj):
        url = (
            reverse('admin:common_players_changelist') + '?'
            + urlencode({'country__id': obj.id})
        )
        return format_html('<a href="{}">{} players</a>', url, obj.players_this_country) 
    
    def image(self, obj):
        if obj.flag.name != '':
            return format_html(f'<img src="{obj.flag.url}" alt="flag image" style="width: 100px"/>')
        return ''
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            players_this_country=Count('players')
        )


@admin.register(models.Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country_name', 'gender', 'created_at')
    list_filter = ('country', 'gender', 'created_at')
    search_fields = ('full_name',)
    autocomplete_fields = ('country', 'position')  

    def country_name(self, obj):
        return obj.country.name
    

@admin.register(models.PlayerPosition)
class PlayerPositionAdmin(TranslationAdmin):
    list_display = ('name_uz', 'name_ru', 'name_en', 'players_this_position')
    search_fields = ('name_uz', 'name_ru', 'name_en')

    def players_this_position(self, obj):
        url = (reverse('admin:common_players_changelist') + '?' + urlencode({'postion__id': obj.id}))
        return format_html('<a href="{}">{} players</a>', url, obj.players_this_position)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            players_this_position=Count('players')
        )
    

@admin.register(models.Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('partner_logo', 'link')

    def partner_logo(self, obj):
        return format_html(f'<img src="{obj.image.url}" alt="partner logo" style="width: 100px"/>')
    
@admin.register(models.AboutCompany)
class AboutCompanyAdmin(TranslationAdmin):
    list_display = ('description', 'created_at')
    list_display_links = ('description',)
    list_filter = ('created_at',)


@admin.register(models.Stadium)
class StadiumAdmin(TranslationAdmin):
    list_display = ('description', 'created_at')
    list_display_links = ('description',)
    search_fields = ('description',)
    list_filter = ('created_at',)


@admin.register(models.Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en', 'banner_link')
    search_fields = ('title_uz', 'title_ru', 'title_en')

    def banner_link(self, obj):
        return format_html(f'<a href="{obj.link}" target="blank">Go to link</a>')
    

@admin.register(models.AboutAcademy)
class AboutAcademyAdmin(TranslationAdmin):
    list_display = ('description_uz', 'description_ru', 'description_en', 'created_at')
    list_display_links = ('description_uz', 'description_ru', 'description_en',)
    list_filter = ('created_at',)
    search_fields = ('description_uz', 'description_ru', 'description_en',)


class CoachInformationInline(TranslationTabularInline):
    model = models.CoachInformation
    extra = 1


@admin.register(models.CoachPosition)
class CoachPositionAdmin(TranslationAdmin):
    list_display = ('name_uz', 'name_ru', 'name_en', 'coaches_this_position')
    search_fields = ('name_uz', 'name_ru', 'name_en')

    def coaches_this_position(self, obj):
        url = (reverse('admin:common_coach_changelist') + '?' + urlencode({'position__id': obj.id}))
        return format_html('<a href="{}">{} coaches</a>', url, obj.coaches_this_position)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            coaches_this_position=Count('coaches')
        )


@admin.register(models.Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'gender',)
    list_select_related = ('position',)
    search_fields = ('full_name',)
    list_filter = ('gender', 'position')
    autocomplete_fields = ('position',)
    inlines = [CoachInformationInline]


@admin.register(models.CoachInformation)
class CoachInformationAdmin(TranslationAdmin):
    list_display = ('name_uz','name_ru', 'name_en', 'coach')
    list_select_related = ('coach',)

    def has_add_permission(self, request):
        return False

@admin.register(models.Leaders)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'country', 'birth_date')
    search_fields = ('full_name', 'position', 'country')