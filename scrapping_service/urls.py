"""scrapping_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from scraping.views import main_view,contact_view,cupons_view,faq_view,indraw_view,my_cupons_view,news_view,profile_view,withdraw_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_view),
    path('contacts/', contact_view),
    path('cupons/', cupons_view),
    path('faq/', faq_view),
    path('indraw/', indraw_view),
    path('my_cupons/', my_cupons_view),
    path('news/', news_view),
    path('profile/', profile_view),
    path('withdraw/', withdraw_view),
]
