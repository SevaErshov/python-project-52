from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from statuses.models import Status
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from statuses.forms import CreationStatusForm
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Task



class StatusesList(View, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'statuses.html', context={'statuses': statuses})


class StatuseCreate( SuccessMessageMixin, CreateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_create.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'
    success_message = 'Статус успешно создан.'


class StatuseUpdate(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_edit.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'
    success_message = 'Статус успешно изменен.'


class StatuseDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'statuse_delete.html'

    model = Status
    fields = ['name']
    success_url = '/statuses/'
    success_message = 'Статус успешно удалён.'
    
    def get(self, request, pk):
        related_task = Task.objects.filter(status=pk)
        if bool(related_task) is True:
            messages.error(request, "Вы не можете удалить статус, так как он связан с задачей.")
            return redirect('/statuses/')
        return render(request, "statuse_delete.html", context={'status': Status.objects.get(id=pk)})