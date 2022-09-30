from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib import messages
from tasks.forms import CreationTaskForm, TaskFilter
from django_filters.views import FilterView




class TasksList(FilterView, LoginRequiredMixin):
    login_url = '/login/'
    filterset_class = TaskFilter
    template_name = 'tasks.html'
    model = Task


class CreateTask(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'task_create.html'

    def post(self, request):
        form = CreationTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.author = User.objects.get(id=request.user.id)
            task.save()
            messages.success(request, "Задача успешно создана")
            return redirect('/tasks/')
        return render(request, 'task_create.html', context={'form': form})

    def get(self, request):
        template = 'task_create.html'
        form = CreationTaskForm()
        return render(request, template, context={'form': form})


class EditTask(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'task_edit.html'

    model = Task
    form_class = CreationTaskForm
    success_url = '/tasks/'
    success_message = 'Задача успешно изменена'


class RemoveTask(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    login_url = '/login/'
    template_name = 'task_delete.html'

    model = Task
    fields = ['name']
    success_url = '/tasks/'
    success_message = 'Задача успешно удалена'

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        if not request.user.id == task.author.id:
            messages.error(request, 'Задачу может удалить только её автор')
            return redirect('/tasks/')
        return render(request, self.template_name, context={'task': task})


class TaskPage(View, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return render(request, 'task.html', context={'task': task, 'labels': task.labels.all()})