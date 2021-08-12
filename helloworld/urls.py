from django.urls.conf import include, path
from . import views


urlpatterns = [
    path('', views.helloWorld)
]
