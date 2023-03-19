from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from base import models
from django.urls import reverse_lazy


class taskList(ListView):
    model = models.Task
    context_object_name = 'tasks'


class taskDetail(DetailView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    model = models.Task
    context_object_name = 'create'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = models.Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'base/prompt.html'
    success_url = reverse_lazy('tasks')
