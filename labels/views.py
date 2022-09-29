from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Task
from labels.models import Label



class LabelsList(View, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request):
        labels = Label.objects.all()
        return render(request, 'labels.html', context={'labels': labels})


class LabelCreate(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'label_create.html'

    model = Label
    fields = ['name']
    success_url = '/labels/'
    success_message = 'Метка успешно создана'


class LabelUpdate(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'label_edit.html'

    model = Label
    fields = ['name']
    success_url = '/labels/'
    success_message = 'Метка успешно изменена'


class LabelDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'label_delete.html'

    model = Label
    fields = ['name']
    success_url = '/labels/'
    success_message = 'Метка успешно удалена'
    
    def get(self, request, pk):
        related_task = Task.objects.filter(labels=pk)
        if bool(related_task) is True:
            messages.error(request, "Невозможно удалить метку, потому что она используется")
            return redirect('/labels/')
        return render(request, "label_delete.html", context={'label': Label.objects.get(id=pk)})