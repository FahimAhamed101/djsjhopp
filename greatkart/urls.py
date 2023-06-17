"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
urlpatterns = i18n_patterns(
      path(_('admin/'), admin.site.urls),

    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
   
    # ORDERS
    path('orders/', include('orders.urls')),
    path('news/', include('news.urls')),
    path('contact/', views.contact, name='contact'),
    path('specialoffer/', views.specialoffer, name='specialoffer'),
     path('accounts/', include('allauth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
     path('rosetta/', include('rosetta.urls')),
       path('config/', views.stripe_config),
      path('create-checkout-session/', views.create_checkout_session),
path('Quotation.html/', views.Quotation,name='Quotation'),
path('Invoice.html/', views.Invoice,name='Invoice'),
path('Receipt.html/', views.Receipt,name='Receipt'),
path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
     path('events/', include('events.urls')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



