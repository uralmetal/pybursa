"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views import generic

from courses.views import home
from contacs.views import ContacsView


urlpatterns = [
    path('quadratic/', include('quadratic.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('coaches/', include('coaches.urls')),
    path('contacs/', ContacsView.as_view(), name='contacs'),
    path('feedback/', include('feedbacks.urls'))
]
