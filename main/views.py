from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.db.models import Q
from .models import Products, Services, ProductRating, ServiceRating, LocationCategory
from django.db.models import Avg
from .filters import LocationCategoryFilter
from django.contrib import messages
from .forms import *


# paystack pay before listing imports

from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.conf import settings
from django.views import View
import logging



# ===========================
# HOME PAGE
# ===========================

class HomePageView(TemplateView):
    template_name = "main/home.html"
    # template_name = "main/index.html"
    context_object_name = "products"
# ===========================
#  PRODUCT VIEWS WITH SEARCH & FILTER
# ===========================


def product_list(request):
    queryset = Products.objects.filter(product_status='published').order_by('-id')  # Filter only published products

    # Filter parameters
    query = request.GET.get("search", "")
    category = request.GET.get("category", "")
    country = request.GET.get("country", "")
    state = request.GET.get("state", "")
    city = request.GET.get("city", "")
    min_rating = request.GET.get("rating", "")

    # Apply filters
    if query:
        queryset = queryset.filter(Q(product_name__icontains=query))
    if category:
        queryset = queryset.filter(product_category__iexact=category)

    if country:
        queryset = queryset.filter(product_country__iexact=country)

    if state:
        queryset = queryset.filter(product_state__iexact=state)

    if city:
        queryset = queryset.filter(product_city__iexact=city)

    if min_rating:
        queryset = queryset.annotate(avg_rating=Avg("product_ratings__rating")).filter(avg_rating__gte=float(min_rating))

    categories = Products.objects.values_list('product_category', flat=True).distinct()
    countries = Products.objects.values_list('product_country', flat=True).distinct()
    states = Products.objects.values_list('product_state', flat=True).distinct()
    cities = Products.objects.values_list('product_city', flat=True).distinct()

    context = {
        "products": queryset,
        "categories": categories,
        "countries": countries,
        "states": states,
        "cities": cities,
        "selected_category": category,
        "selected_country": country,
        "selected_state": state,
        "selected_city": city,
        "selected_rating": min_rating,
    }

    return render(request, "main/products_list.html", context)


class ProductDetailView(DetailView):
    model = Products
    template_name = "main/product_details.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = self.object.product_ratings.all()
        context['average_rating'] = self.object.average_rating()
        context['rating_count'] = self.object.rating_count()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = "main/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        product = form.save(commit=False)  # Prevent immediate save
        product.product_status = 'pending'  # Ensure status is set explicitly
        
        try:
            product.save()  # Save the service
            return redirect('pay_product_listing', product_id=product.id)
        except Exception as e:
            form.add_error(None, f"An error occurred: {str(e)}")  # Add error to form
            return self.form_invalid(form)  # Handle failure case


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    template_name = "main/product_form.html"
    fields = "__all__"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = "main/product_delete.html"
    success_url = reverse_lazy("product_list")


def service_list(request):
    queryset = Services.objects.filter(service_status='published').order_by('-id')  # Filter only published services

    # Filter parameters
    query = request.GET.get("search", "")
    category = request.GET.get("category", "")
    country = request.GET.get("country", "")
    state = request.GET.get("state", "")
    city = request.GET.get("city", "")
    min_rating = request.GET.get("rating", "")

    # Apply filters
    if query:
        queryset = queryset.filter(Q(service_name__icontains=query))

    if category:
        queryset = queryset.filter(service_category__iexact=category)

    if country:
        queryset = queryset.filter(service_country__iexact=country)

    if state:
        queryset = queryset.filter(service_state__iexact=state)

    if city:
        queryset = queryset.filter(service_city__iexact=city)

    if min_rating:
        queryset = queryset.annotate(avg_rating=Avg("service_ratings__rating")).filter(avg_rating__gte=float(min_rating))

    categories = Services.objects.values_list('service_category', flat=True).distinct()
    countries = Services.objects.values_list('service_country', flat=True).distinct()
    states = Services.objects.values_list('service_state', flat=True).distinct()
    cities = Services.objects.values_list('service_city', flat=True).distinct()

    context = {
        "services": queryset,
        "categories": categories,
        "countries": countries,
        "states": states,
        "cities": cities,
        "selected_category": category,
        "selected_country": country,
        "selected_state": state,
        "selected_city": city,
        "selected_rating": min_rating,
    }

    return render(request, "main/services_list.html", context)


class ServiceDetailView(DetailView):
    model = Services
    template_name = "main/service_details.html"
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = self.object.service_ratings.all()
        context['average_rating'] = self.object.average_rating()
        context['rating_count'] = self.object.rating_count()
        return context


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Services
    template_name = "main/service_form.html"
    form_class = ServiceForm
    success_url = reverse_lazy("service_list")

    def form_valid(self, form):
        service = form.save(commit=False)  # Prevent immediate save
        service.service_status = 'pending'  # Ensure status is set explicitly
        
        try:
            service.save()  # Save the service
            return redirect('pay_service_listing', service_id=service.id)
        except Exception as e:
            form.add_error(None, f"An error occurred: {str(e)}")  # Add error to form
            return self.form_invalid(form)  # Handle failure case

class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    template_name = "main/service_form.html"
    fields = "__all__"
    success_url = reverse_lazy("service_list")


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = "main/service_delete.html"
    success_url = reverse_lazy("service_list")


# ===========================
#  PRODUCT RATING VIEW
# ===========================

class ProductRatingCreateView(LoginRequiredMixin, CreateView):
    model = ProductRating
    template_name = "main/product_rating_form.html"
    fields = ['rating', 'review']  # Removed 'product' since we fetch it from URL

    def form_valid(self, form):
        product_id = self.kwargs['pk']  # Get product ID from URL
        product = Products.objects.get(pk=product_id)  # Fetch product from DB
        user = self.request.user

        # Check if user already rated this product
        existing_rating = ProductRating.objects.filter(product=product, user=user).first()
        if existing_rating:
            existing_rating.rating = form.cleaned_data['rating']
            existing_rating.review = form.cleaned_data['review']
            existing_rating.save()
            messages.success(self.request, "Your rating has been updated.")
        else:
            form.instance.user = user
            form.instance.product = product  # Assign product to the rating
            form.save()
            messages.success(self.request, "Your rating has been submitted.")

        return redirect(reverse('product_detail', kwargs={'pk': product_id}))

# ===========================
#  SERVICE RATING VIEW
# ===========================

class ServiceRatingCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRating
    template_name = "main/service_rating_form.html"
    fields = ['rating', 'review']  # Removed 'service' since we fetch it from URL

    def form_valid(self, form):
        service_id = self.kwargs['pk']  # Get service ID from URL
        service = Services.objects.get(pk=service_id)  # Fetch service from DB
        user = self.request.user

        # Check if user already rated this service
        existing_rating = ServiceRating.objects.filter(service=service, user=user).first()
        if existing_rating:
            existing_rating.rating = form.cleaned_data['rating']
            existing_rating.review = form.cleaned_data['review']
            existing_rating.save()
            messages.success(self.request, "Your rating has been updated.")
        else:
            form.instance.user = user
            form.instance.service = service  # Assign service to the rating
            form.save()
            messages.success(self.request, "Your rating has been submitted.")

        return redirect(reverse('service_detail', kwargs={'pk': service_id}))



# Paystack pay before listing view

class PaystackListingPaymentView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id', None)  # If it's a product
        service_id = self.kwargs.get('service_id', None)  # If it's a service

        # Listing Fee (example fee of 1000)
        listing_fee = 1000  # in kobo (1000 kobo = 10 Naira)

        # Set the appropriate name and amount depending on whether it's a product or service
        if product_id:
            item_name = "Product Listing Fee"
            order_id = product_id
        elif service_id:
            item_name = "Service Listing Fee"
            order_id = service_id
        else:
            messages.error(request, "Invalid request.")
            return redirect('home')

        email = request.user.email

        # Paystack Payment Initialization
        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
        }

        # Create Payment Request
        data = {
            'amount': listing_fee,
            'email': email,
            'callback_url': 'https://127.0.0.1:8000/payment/callback/',  # Set this to your callback URL
            'order_id': order_id,
            'name': item_name,
        }

        response = requests.post(settings.PAYSTACK_PAYMENT_URL, json=data, headers=headers)

        if response.status_code == 200:
            payment_data = response.json()
            authorization_url = payment_data['data']['authorization_url']
            return redirect(authorization_url)
        else:
            messages.error(request, "Payment initialization failed. Please try again.")
            return redirect('home')




class PaystackCallbackView(View):
    def get(self, request, *args, **kwargs):
        ref = request.GET.get('reference')  # Paystack payment reference
        
        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
        }
        
        # Verify payment
        verify_url = f'https://api.paystack.co/transaction/verify/{ref}'
        response = requests.get(verify_url, headers=headers)

        if response.status_code == 200:
            verification_data = response.json()
            status = verification_data['data']['status']
            
            if status == 'success':
                # Payment was successful, update listing status
                order_id = verification_data['data']['order_id']
                
                # Update Product status
                if Products.objects.filter(id=order_id).exists():
                    product = Products.objects.get(id=order_id)
                    product.product_status = 'published'  # Update status to published
                    product.save()
                    messages.success(request, "Payment Successful. Your product is now listed.")

                # Update Service status
                elif Services.objects.filter(id=order_id).exists():
                    service = Services.objects.get(id=order_id)
                    service.service_status = 'published'  # Update status to published
                    service.save()
                    messages.success(request, "Payment Successful. Your service is now listed.")
            else:
                messages.error(request, "Payment failed. Please try again.")
        else:
            messages.error(request, "Error verifying payment.")
        
        return redirect('home')
