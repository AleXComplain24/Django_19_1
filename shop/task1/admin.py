from django.contrib import admin
from .models import Game, Buyer


# Админ-класс для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Фильтрация по полям size и cost
    list_filter = ('size', 'cost')

    # Отображение полей title, cost и size при отображении всех записей
    list_display = ('title', 'cost', 'size')

    # Поиск по полю title
    search_fields = ('title',)

    # Ограничение количества записей до 20
    list_per_page = 20


# Админ-класс для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Фильтрация по полям balance и age
    list_filter = ('balance', 'age')

    # Отображение полей name, balance и age при отображении всех записей
    list_display = ('name', 'balance', 'age')

    # Поиск по полю name
    search_fields = ('name',)

    # Ограничение количества записей до 30
    list_per_page = 30

    # Поле balance только для чтения
    readonly_fields = ('balance',)
