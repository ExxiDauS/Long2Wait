from django.urls import path
from . import views

# pull function from views
# path(path, where to pull, name)
urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings')
]
