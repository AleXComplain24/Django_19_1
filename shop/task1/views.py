from django.shortcuts import render

from django.shortcuts import render
from .models import Game

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