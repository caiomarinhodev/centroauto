from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, DeleteView, CreateView, DetailView

from app.forms import ClienteForm
from app.models import Cliente


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    context_object_name = 'cliente'
    form_class = ClienteForm
    template_name = 'clientes/edit.html'
    success_url = '/'


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    ordering = '-created_at'
    template_name = 'clientes/list.html'


class ClienteDelete(DeleteView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'clientes/delete.html'
    success_url = '/'


class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/create.html'
    success_url = '/'


class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'clientes/create.html'