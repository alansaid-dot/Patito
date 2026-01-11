from django.urls import path
from .import views
from applications.home.views import test_ok

urlpatterns = [
    path('home/', views.indexView.as_view()),
    path('foundation/', views.FoundationView.as_view()),
    path('lista/', views.PruebalistView.as_view()),
    path('prueba_lita/', views.ModeloPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
     path('', test_ok),
]