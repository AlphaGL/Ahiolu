from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect,render
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from main.models import Products, Services


# ===========================
#  USET LOGIN  VIEW
# ===========================
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid email or password. Please try again.")
        return super().form_invalid(form)

# ===========================
#  USET LOGOUT  VIEW
# ===========================
def logout_user(request):
    logout(request)
    return redirect('login')


# ===========================
#  USET REGISTER  VIEW
# ===========================
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Registration successful. Please log in.")
        return response


# ===========================
#  EDIT PRODUCT OR SERVICE  VIEW
# ===========================
@login_required
def user_dashboard(request):
    # Get all products (regular and promoted) posted by the logged-in user
    products = Products.objects.filter(user=request.user)
    promoted_products = Products.objects.filter(user=request.user, is_promoted=True)  # Assuming 'is_promoted' field

    # Get all services (regular and promoted) posted by the logged-in user
    services = Services.objects.filter(user=request.user)
    promoted_services = Services.objects.filter(user=request.user, is_promoted=True)  # Assuming 'is_promoted' field

    return render(request, 'users/dashboard.html', {
        'products': products,
        'promoted_products': promoted_products,
        'services': services,
        'promoted_services': promoted_services,
    })

