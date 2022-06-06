from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
# import models
from .models import Client


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class ClientList(TemplateView):
    template_name = "client_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["clients"] = Client.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["clients"] = Client.objects.all()
            context["header"] = "Clients"
        return context


class ClientCreate(CreateView):
    model = Client
    fields = ['status', 'name', 'position', 'image', 'email',
              'phone', 'resume', 'linkedin', 'notes']
    template_name = "client_create.html"
    success_url = "/clients/"


class ClientDetail(DetailView):
    model = Client
    template_name = "client_detail.html"


class ClientUpdate(UpdateView):
    model = Client
    fields = ['status', 'name', 'position', 'image', 'email',
              'phone', 'resume', 'linkedin', 'notes']
    template_name = "client_update.html"

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.pk})


class ClientDelete(DeleteView):
    model = Client
    template_name = "client_delete.html"
    success_url = "/clients/"
