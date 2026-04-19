from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/create/', views.create_article, name='create_article'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),  # ← ДОБАВЬ ЭТУ СТРОЧКУ
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/<int:news_id>/edit/', views.edit_news, name='edit_news'),
    path('news/<int:news_id>/delete/', views.delete_news, name='delete_news'),
    path('about/', views.about, name='about'),
    path('connection/', views.connection, name='connection'),
    path('sign/', views.register, name='sign'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
]