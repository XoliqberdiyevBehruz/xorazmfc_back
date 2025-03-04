from rest_framework import serializers

from common import models


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsCategory
        fields = ('id', 'name_uz', 'name_ru', 'name_en')


class NewsSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(method_name='get_date')
    category_name = serializers.SerializerMethodField(method_name='get_category_name')

    class Meta:
        model = models.News
        fields = ('id', 'slug', 'title_uz', 'title_ru', 'title_en', 'image', 'date', 'category_name')
    
    def get_date(self, obj):
        return obj.created_at.date()
    
    def get_category_name(self, obj):
        return obj.category.name


class NewsDetailSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(method_name='get_date')

    class Meta:
        model = models.News
        fields = ('id', 'slug', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'image', 'date')
    
    def get_date(self, obj):
        return obj.created_at.date()
    

class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Players
        fields = (
            'id', 'full_name', 'number', 'image', 'gender'
        )
    

class PlayerPosiotionListSerializer(serializers.ModelSerializer):
    players = PlayerListSerializer(many=True)

    class Meta:
        model = models.PlayerPosition
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'players')


class PlayerCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerCountry
        fields = ('id', 'flag', 'name')


class PlayerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerPosition
        fields = ('id', 'name_uz', 'name_ru', 'name_en')


class PlayerDetailSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField(method_name='get_country')
    position = serializers.SerializerMethodField(method_name='get_position')

    class Meta:
        model = models.Players
        fields = (
            'id', 'full_name', 'number', 'image', 'goal', 'match', 
            'assist', 'birth_date', 'height', 'description_uz', 
            'description_ru', 'description_en', 'country', 'gender', 'position'
        )

    def get_country(self, obj):
        return PlayerCountrySerializer(obj.country).data
    
    def get_position(self, obj):
        return PlayerPositionSerializer(obj.position).data
    

class PartnerLogoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partners
        fields = ('id', 'image', 'link')
    

class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutCompany
        fields = ('id', 'description_uz', 'description_ru', 'description_en', 'image')


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stadium
        fields = ('id', 'image', 'description_uz', 'description_ru', 'description_en')

    
class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'banner', 'link')

    
class AboutAcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutAcademy
        fields = ('id', 'description_uz', 'description_ru', 'description_en', 'image', 'created_at')


class CoachPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoachPosition
        fields = ('id', 'name_uz', 'name_ru', 'name_en')


class CoachListSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField(method_name='get_position')

    class Meta:
        model = models.Coach
        fields = ('id', 'full_name', 'position', 'image')

    def get_position(self, obj):
        return CoachPositionSerializer(obj.position).data


class CoachInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoachInformation
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'value_uz', 'value_ru', 'value_en')


class CoachDetailSerializer(serializers.ModelSerializer):
    position = CoachPositionSerializer()
    infos = serializers.SerializerMethodField(method_name='get_infos')

    class Meta:
        model = models.Coach
        fields = (
            'id', 'full_name', 'image', 'banner', 'position', 'infos'
        )

    def get_infos(self, obj):
        return CoachInformationSerializer(obj.informations, many=True).data
    

class CoachTableListSerializer(serializers.ModelSerializer):    
    position = serializers.SerializerMethodField(method_name='get_position')

    class Meta:
        model = models.Coach
        fields = (
            'id', 'full_name', 'position'
        )
    
    def get_position(self, obj):
        return CoachPositionSerializer(obj.position).data
    

class LeaderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leaders
        fields = ('id', 'full_name', 'image', 'position', 'country', 'birth_date')

    
class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=100)
