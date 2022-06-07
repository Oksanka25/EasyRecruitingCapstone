from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
# import models
from .models import Client, Interview
# auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


@method_decorator(login_required, name='dispatch')
class ClientList(TemplateView):
    template_name = "client_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["clients"] = Client.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["clients"] = Client.objects.filter(user=self.request.user)
            context["header"] = "Clients"
        return context


@method_decorator(login_required, name='dispatch')
class ClientCreate(CreateView):
    model = Client
    fields = ['status', 'name', 'position', 'image', 'email',
              'phone', 'resume', 'linkedin', 'notes']
    template_name = "client_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClientCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('client_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    model = Client
    template_name = "client_detail.html"


@method_decorator(login_required, name='dispatch')
class ClientUpdate(UpdateView):
    model = Client
    fields = ['status', 'name', 'position', 'image', 'email',
              'phone', 'resume', 'linkedin', 'notes']
    template_name = "client_update.html"

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ClientDelete(DeleteView):
    model = Client
    template_name = "client_delete.html"
    success_url = "/clients/"


@method_decorator(login_required, name='dispatch')
class InterviewCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        company = request.POST.get("company")
        date = request.POST.get("date")
        feedback = request.POST.get("feedback")
        result = request.POST.get("result")
        notes = request.POST.get("notes")
        client = Client.objects.get(pk=pk)
        Interview.objects.create(
            title=title, company=company, date=date, feedback=feedback, result=result, notes=notes, client=client)
        return redirect('client_detail', pk=pk)


@method_decorator(login_required, name='dispatch')
class InterviewUpdate(UpdateView):
    model = Interview
    fields = ['title', 'company', 'date', 'feedback', 'result', 'notes']
    template_name = "interview_update.html"

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.client_id})


@method_decorator(login_required, name='dispatch')
class InterviewDelete(DeleteView):
    model = Interview
    template_name = "interview_delete.html"

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.client_id})


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("client_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
