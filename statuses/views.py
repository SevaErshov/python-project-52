from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from statuses.models import Status
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Task


class StatusesList(View, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'statuses.html', context={'statuses': statuses})


class StatuseCreate(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_create.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'
    success_message = 'Статус успешно создан'


class StatuseUpdate(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_edit.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'
    success_message = 'Статус успешно изменён'


class StatuseDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_delete.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'

    def post(self, request, pk, *args, **kwargs):
        related_task = Task.objects.filter(status=pk)
        if bool(related_task) is True:
            messages.error(request, "Невозможно удалить статус, потому что он используется")
            return redirect('/statuses/')
        messages.success(request, 'Статус успешно удалён')
        return self.delete(request, *args, **kwargs)

    def get(self, request, pk):
        return render(request, "statuse_delete.html", context={'status': Status.objects.get(id=pk)})
