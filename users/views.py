from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


context = {
    'Users': _("Users"),
    'Name': _("Name"),
    'Created': _("Created"),
    'UserName': _("UserName"),
    'Edit': _("Edit"),
    'Delete': _("Delete"),
    'FirstName': _("FirstName"),
    'LastName': _("LastName"),
    'Confirm': _("Confirm"),
    'Password': _("Password"),
    'Submit': _("Submit"),
    'SignUp': _("SignUp"),
    'Log_in': _("Log_in"),
    'LogIn': _("LogIn"),
    'LogOut': _("LogOut"),
    'EditUser': _("EditUser"),
    'DeleteUser': _("DeleteUser"),
    'ConfirmDelete': _("ConfirmDelete"),
    'ConfirmDeleteButton': _("ConfirmDeleteButton"),
    'Statuses': _("Statuses"),
}


class UsersPage(View):

    def get(self, request):
        if request.user.is_authenticated:
            template = 'users_a.html'
        else:
            template = 'users.html'
        users = User.objects.all()
        context['users'] = users
        return render(request, template, context=context)


class Create(FormView):
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect('/login/')
        context['form'] = form
        return render(request, 'create_user.html', context=context)

    def get(self, request):
        template = 'create_user.html'
        form = RegisterForm()
        context['form'] = form
        return render(request, template, context=context)


class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы залогинены')
            return redirect('/')
        else:
            messages.error(request, """Пожалуйста, введите правильные имя пользователя и пароль.
            Оба поля могут быть чувствительны к регистру.""")
            return render(request, 'login.html', context=context)

    def get(self, request):
        if request.user.is_authenticated:
            template = 'login_a.html'
        else:
            template = 'login.html'
        form = LoginForm()
        context['form'] = form
        return render(request, template, context=context)


class LogOut(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'Вы разлогинены')
        return redirect('/')


class EditUser(SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'

    model = User
    form_class = RegisterForm
    success_url = '/users/'
    success_message = 'Пользователь успешно изменён'

    def get(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect('/login/')
        if not request.user.id == pk:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('/users/')
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)


class RemoveUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'delete.html'

    success_url = ('/users/')
    success_message = 'Пользователь успешно удалён'

    def get(self, request, pk):
        if not request.user.is_authenticated:
            messages.error(request, 'Вы не авторизованы. Пожалуйста, выполните вход.')
            return redirect('/login/')
        if not request.user.id == pk:
            messages.error(request, 'У вас нет прав для редактирования других пользователей.')
            return redirect('/users/')
        context['user'] = request.user
        return render(request, self.template_name, context=context)
