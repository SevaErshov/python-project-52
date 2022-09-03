from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style=\" font-size: 200px;\">Я фанат Михаила Лабковского и сериала \'Доктор Хаус\'!</h1>")