from django.urls import path
from . import views

urlpatterns = [
    path('', views.platform, name='platform'),  # Главная страница
    path('registration/', views.registration_page, name='registration_page'),  # Страница регистрации
    path('cart/', views.cart, name='cart'),  # Корзина
    path('games/', views.games, name='games'), # Список игр
    path('news/', views.news, name='news'),  # Новая страница новостей
]