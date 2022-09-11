from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View


class Index(View):

    def get(self, request):
        return render(request, 'index.html')
