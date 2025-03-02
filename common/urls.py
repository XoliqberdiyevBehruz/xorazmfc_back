from django.urls import path

from common import views

urlpatterns = [
    # news urls
    path('news/category/list/', views.NewsCategoryListApiView.as_view()),
    path('news/category/<uuid:id>/', views.NewsListApiView.as_view()),
    path('news/<slug:slug>/', views.NewsDetailApiView.as_view()),
    # player urls
    path('players/man/', views.PlayerManListApiView.as_view()),
    path('players/women/', views.PlayerWomanListApiView.as_view()),
    path('players/u19/', views.PlayerU19ListApiView.as_view()),
    path('players/u21/', views.PlayerU21ListApiView.as_view()),

    path('players/<uuid:id>/', views.PlayerDetailApiView.as_view()),
    
    path('partners/', views.PartnerListApiView.as_view()),
    
    path('about-club/', views.AboutCompanyApiView.as_view()),
    
    path('stadiums/', views.StadiumListApiView.as_view()),
    
    path('banners/', views.BannerListApiView.as_view()),
    
    path('about-academy/list/', views.AboutAcademyApiView.as_view()),
    # coach urls
    path('coach/list/man/', views.CoachListManApiView.as_view()),
    path('coach/list/women/', views.CoachListWomenApiView.as_view()),
    path('coach/<uuid:id>/', views.CoachDetailApiView.as_view()),  
    path('coach/table/list/man/', views.CoachTableListManApiView.as_view()),
    path('coach/table/list/women/', views.CoachTableListWomenApiView.as_view()),
    path('coach/list/academy/', views.CoachAcademyListApiView.as_view()),

    # leaders
    path('leaders/list/', views.LeaderListApiView.as_view()),
]
