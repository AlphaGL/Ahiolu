from django.urls import path
from .views import (
    product_list, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    service_list, ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView,
    ProductRatingCreateView, ServiceRatingCreateView,HomePageView,PaystackListingPaymentView,PaystackCallbackView
)

urlpatterns = [ 
    # Home URL
    path('', HomePageView.as_view(), name='home'),

    # Product URLs
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/rate/', ProductRatingCreateView.as_view(), name='product_rate'),

    # Service URLs
    path('services/', service_list, name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/new/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    path('services/<int:pk>/rate/', ServiceRatingCreateView.as_view(), name='service_rate'),


    # Paystack URLs
    path('products/<int:product_id>/pay/', PaystackListingPaymentView.as_view(), name='pay_product_listing'),
    path('services/<int:service_id>/pay/', PaystackListingPaymentView.as_view(), name='pay_service_listing'),
    path('payment/callback/', PaystackCallbackView.as_view(), name='paystack_callback'),
]
