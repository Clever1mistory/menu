from django.shortcuts import render


# Представление для отображения страницы с меню
def home(request):
    return render(request, 'base.html')
