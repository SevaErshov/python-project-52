from django.shortcuts import render
from django.views import View
from users.models import Users
from django.utils.translation import gettext as _

context = {
    'Users': _("Users"),
    'Name': _("Name"),
    'Created': _("Created"),
    'UserName': _("UserName"),
    'Edit': _("Edit"),
    'Delete': _("Delete"),
    'FirstName': _("FirstName"),
    'LastName': _("LastName"),
    'ForPassword': _("ForPassword"),
    'ForConfirm': _("ForConfirm"),
    'Confirm': _("Confirm"),
    'Password': _("Password"),
    'ForUserName': _("ForUserName"),
    'Submit': _("Submit"),
    'SignUp': _("SignUp"),
    'Log_in': _("Log_in"),
    'LogIn': _("LogIn"),
}


class UsersPage(View):

    def get(self, request):
        users = Users.objects.order_by('created_at')
        context['users'] = users
        return render(request, 'users.html', context=context)


class Create(View):

    def get(self, request):
        return render(request, 'create_user.html', context=context)


class Login(View):

    def get(self, request):
        return render(request, 'login.html', context=context)