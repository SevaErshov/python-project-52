from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

def index(request):
    context = {
        'Users': _('Users'),
        'SignUp': _('SignUp'),
        'LogIn': _('LogIn'),
    }
    return render(request, 'index.html', context=context)
