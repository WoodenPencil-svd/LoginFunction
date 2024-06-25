from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, RedirectView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm




class HomeView(TemplateView):
    template_name = 'home/index.html'
    

class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
      form = self.get_form()
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
      return self.render_to_response(self.get_context_data(form=form))

    


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
    
    
