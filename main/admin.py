from django.contrib import admin
from .models import *

admin.site.register(LocationCategory)
admin.site.register(Products)
admin.site.register(Services)
admin.site.register(ProductRating)
admin.site.register(ServiceRating)




# i am creating a plateform, whereby users can post their products or render services but they have to make payment before their products or services are set from pending to publish, and also i integrated a paystack payment system code that users post [ products or services ] can only be set to publish after the have made payment and the payment is successful. but after payement, it is not setting it to publish. i will send u my code, change the views to function based views and impement the logic well