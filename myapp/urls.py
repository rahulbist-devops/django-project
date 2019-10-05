from django.urls import  path
from myapp import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]