from django.shortcuts import render

from django.shortcuts import render
from .models import Game
from django.core.paginator import Paginator
from .models import News

def platform(request):
    return render(request, 'task1/templates/fourth_task/platform.html')  # Новый путь

def registration_page(request):
    if request.method == 'POST':
        form = Registration_page(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # Проверка, существует ли покупатель с таким именем
            if not Buyer.objects.filter(username=username).exists():
                # Создаём нового покупателя
                Buyer.objects.create(
                    username=username,
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']  # Добавляем пароль
                )
                return redirect('platform')  # Перенаправляем на главную страницу
            else:
                form.add_error('username', 'Пользователь с таким именем уже существует.')
    else:
        form = Registration_page()
    return render(request, 'task1/templates/fifth_task/registration_page.html', {'form': form})  # Новый путь

def cart(request):
    return render(request, 'shop/task1/templates/fourth_task/cart.html')  # Шаблон корзины

def games(request):
    games = Game.objects.all()  # Получаем все игры
    return render(request, 'task1/templates/fourth_task/games.html', {'games': games})  # Новый путь

def news(request):
    news_list = News.objects.all().order_by('-date')  # Сортируем по дате, последние новости первыми
    paginator = Paginator(news_list, 5)  # Показываем 5 новостей на странице

    page_number = request.GET.get('page')  # Получаем номер страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'task1/news.html', {'news': page_obj})
