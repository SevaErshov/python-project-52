from django.shortcuts import render
from django.views import View


class Index(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index_a.html')
        else:
            return render(request, 'index.html')
