"""iguessso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import iguessso_app.views

app_name = 'iguessso_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', iguessso_app.views.total_distinguish, name='total_distinguish'),
    path('total_distinguish/', iguessso_app.views.grade_table, name='grade_table'),
    path('detail_distinguish/', iguessso_app.views.detail_distinguish, name='detail_distinguish'),
]
