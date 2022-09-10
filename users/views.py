from django.shortcuts import render
from django.views import View
from users.models import User
from django.utils.translation import gettext as _

context = {
    'Users': _("Users"),
    'Name': _("Name"),
    'Created': _("Created"),
    'UserName': _("UserName"),
    'Edit': _("Edit"),
    'Delete': _("Delete"),
}

class Users(View):

    def get(self, request):
        users = User.objects.order_by('created_at')
        context['users'] = users
        return render(request, 'users.html', context=context)
