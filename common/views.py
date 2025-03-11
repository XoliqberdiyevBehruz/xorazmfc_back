from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page 
from django.core.cache import cache
from django.db.models import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView

from common import models, serializers, pagination

class NewsCategoryListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='news_category_list_cache'))
    def get(self, request):
        categories = models.NewsCategory.objects.values('id', 'name_uz', 'name_ru', 'name_en').order_by('created_at')
        serializer = serializers.NewsCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class NewsListApiView(ListAPIView):
    serializer_class = serializers.NewsSerializer
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        category = models.NewsCategory.objects.filter(id=self.kwargs.get('id'))
        if not category:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        return models.News.objects.filter(category_id=self.kwargs.get('id')).select_related('category').order_by('-created_at')
   
    @method_decorator(cache_page(2*60, key_prefix='news_list_cache'))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsDetailApiView(RetrieveAPIView):
    serializer_class = serializers.NewsDetailSerializer

    @method_decorator(cache_page(2*60, key_prefix='news_detail_cache'))
    def retrieve(self, request, *args, **kwargs):
        news = models.News.objects.filter(slug=self.kwargs.get('slug')).first()
        if not news:
            return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.NewsDetailSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PlayerManListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='player_list_cache'))
    def get(self, request):
        players = models.PlayerPosition.objects.prefetch_related(Prefetch('players', queryset=models.Players.objects.filter(gender=models.MAN))).order_by('created_at')
        serializer = serializers.PlayerPosiotionListSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayerWomanListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='player_list_cache'))
    def get(self, request):
        players = models.PlayerPosition.objects.prefetch_related(Prefetch('players', queryset=models.Players.objects.filter(gender=models.WOMEN))).order_by('created_at')
        serializer = serializers.PlayerPosiotionListSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PlayerU19ListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='player_list_cache'))
    def get(self, request):
        players = models.PlayerPosition.objects.prefetch_related(Prefetch('players', queryset=models.Players.objects.filter(gender=models.U19))).order_by('created_at')
        serializer = serializers.PlayerPosiotionListSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PlayerU21ListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='player_list_cache'))
    def get(self, request):
        players = models.PlayerPosition.objects.prefetch_related(Prefetch('players', queryset=models.Players.objects.filter(gender=models.U21))).order_by('created_at')
        serializer = serializers.PlayerPosiotionListSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PlayerDetailApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='player_detail_cache'))
    def get(self, request, id):
        player = models.Players.objects.select_related('position', 'country').filter(id=id).first()
        if not player:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.PlayerDetailSerializer(player)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PartnerListApiView(APIView):
    @method_decorator(cache_page(2*60, key_prefix='partner_list_cache'))
    def get(self, request):
        queryset = models.Partners.objects.all().order_by('created_at')
        serializer = serializers.PartnerLogoListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutCompanyApiView(ListAPIView):
    serializer_class = serializers.AboutCompanySerializer

    @method_decorator(cache_page(2*60, key_prefix='about_company_list_cache'))
    def list(self, request, *args, **kwargs):   
        queryset = models.AboutCompany.objects.all().order_by('created_at')
        serializer = serializers.AboutCompanySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StadiumListApiView(ListAPIView):
    serializer_class = serializers.StadiumSerializer

    @method_decorator(cache_page(2*60, key_prefix='stadium_list_cache'))
    def list(self, request, *args, **kwargs):
        queryset = models.Stadium.objects.all().order_by('created_at')
        serializer = serializers.StadiumSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BannerListApiView(ListAPIView):
    serializer_class = serializers.BannerListSerializer

    @method_decorator(cache_page(2*60, key_prefix='banner_list_cache'))
    def list(self, request, *args, **kwargs):
        queryset = models.Banner.objects.all().order_by('created_at')
        serializer = serializers.BannerListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutAcademyApiView(ListAPIView):
    serializer_class = serializers.AboutAcademySerializer
    
    @method_decorator(cache_page(2*60, key_prefix='about_academy_list_cache'))
    def list(self, request, *args, **kwargs):
        data = models.AboutAcademy.objects.all().order_by('created_at')
        serializer = serializers.AboutAcademySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CoachListManApiView(ListAPIView):
    serializer_class = serializers.CoachListSerializer
    queryset = models.Coach.objects.filter(gender=models.MAN, coach_type=models.TEAM_COACH).only(
        'id', 'full_name', 'image', 'position_id'
    ).select_related('position').order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='coach_list_man_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class CoachListWomenApiView(ListAPIView):
    serializer_class = serializers.CoachListSerializer
    queryset = models.Coach.objects.filter(gender=models.WOMEN, coach_type=models.TEAM_COACH).only(
        'id', 'full_name', 'image', 'position_id'
    ).select_related('position').order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='coach_list_woman_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class CoachDetailApiView(RetrieveAPIView):
    serializer_class = serializers.CoachDetailSerializer
    queryset = models.Coach.objects.select_related('position').order_by('created_at')
    lookup_field = 'id'

    @method_decorator(cache_page(2*60, key_prefix='coach_detail_cache'))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    

class CoachTableListManApiView(ListAPIView):
    serializer_class = serializers.CoachTableListSerializer
    queryset = models.Coach.objects.filter(gender=models.MAN).only('id', 'full_name', 'position_id').select_related('position').order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='coach_table_list_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class CoachTableListWomenApiView(ListAPIView):
    serializer_class = serializers.CoachTableListSerializer
    queryset = models.Coach.objects.filter(gender=models.WOMEN).only('id', 'full_name', 'position_id').select_related('position').order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='coach_table_list_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class CoachAcademyListApiView(ListAPIView):
    serializer_class = serializers.CoachListSerializer
    queryset = models.Coach.objects.filter(coach_type=models.ACADEMY_COACH).select_related('position').order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='coach_academy_list_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class LeaderListApiView(ListAPIView):
    serializer_class = serializers.LeaderListSerializer
    queryset = models.Leaders.objects.order_by('created_at')

    @method_decorator(cache_page(2*60, key_prefix='leader_list_cache'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class SearchApiView(GenericAPIView):   
    serializer_class = serializers.SearchSerializer

    def post(self, request):
        serializer = serializers.SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        news = models.News.objects.filter(title__icontains=serializer.validated_data['search'])[:5]
        players = models.Players.objects.filter(full_name__icontains=serializer.validated_data['search'])[:5]
        coaches = models.Coach.objects.filter(full_name__icontains=serializer.validated_data['search'])[:5]
        leaders = models.Leaders.objects.filter(full_name__icontains=serializer.validated_data['search'])[:5]
        data = {
            "news": serializers.NewsSerializer(news, many=True).data,  
            "players": serializers.PlayerListSerializer(players, many=True).data,
            "coaches": serializers.CoachListSerializer(coaches, many=True).data,
            "leaders": serializers.LeaderListSerializer(leaders, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)