from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
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
