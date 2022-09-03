from django.http import HttpResponse


def index(request):
    return HttpResponse("Я фанат Михаила Лабковского и сериала \'Доктор Хаус\'!")