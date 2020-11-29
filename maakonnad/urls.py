from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'maakonnad'

urlpatterns = [
    path('', views.test_view, name='test')
]