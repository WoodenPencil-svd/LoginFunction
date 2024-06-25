from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'
    
class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect(self.get_success_url())
        else:
            return HttpResponse('Cannot find user, Do you have account yet ?')

class LogoutView(RedirectView):
    url = reverse_lazy('home')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
