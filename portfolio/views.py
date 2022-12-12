
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Project
from django.views.generic import  CreateView
from portfolio.forms import RegistroUserForm, NewUserForm,PortfolioProyectForm
from django.urls import reverse, reverse_lazy


def home(request):
    projects = Project.objects.all()
    forms= PortfolioProyectForm()
    return render(request, "home.html", {"projects": projects,"formulario": forms})

class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm
  def form_valid(self, form):
        form.save()
        return redirect('login')

class CreateProjectView(CreateView):
  template_name = "createpy.html"
  model= Project
  fields= ["title", "description", "image", "url", "tag"]
  success_url = reverse_lazy('portfolio:home')
