from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import CustomUser, HomeLocation, Location

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'
    extra_context = {
        'location_count': Location.objects.all().count(),
        'user_count': CustomUser.objects.all().count(),
    }

class SignupPageView(LoginRequiredMixin, generic.CreateView):
    form_class= CustomUserCreationForm
    success_url = reverse_lazy('all_users')
    template_name = 'registration/signup.html'

class UserView(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    template_name = 'v_users.html'

class AddLocationView(LoginRequiredMixin, generic.CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('all_location')
    template_name: str = 'a_location.html'

class LocationView(LoginRequiredMixin, generic.ListView):
    model = Location
    success_url = reverse_lazy('all_location')
    template_name: str = 'all_location.html'

class LocationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Location
    success_url = reverse_lazy('all_location')
    template_name: str = 'delete_location.html'

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CustomUser
    context_object_name = 'user'
    success_url = reverse_lazy('all_users')
    template_name: str = 'delete_user.html'

class AddHomeView(LoginRequiredMixin, generic.CreateView):
    model = HomeLocation
    fields = '__all__'
    success_url = reverse_lazy('all_home')
    template_name: str = 'a_home_location.html'

class HomeLocationView(LoginRequiredMixin, generic.ListView):
    model = HomeLocation
    template_name: str = 'all_home_location.html'

class HomeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = HomeLocation
    context_object_name = 'home'
    success_url = reverse_lazy('all_home')
    template_name: str = 'delete_home_location.html'