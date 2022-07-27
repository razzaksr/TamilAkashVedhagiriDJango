from django.urls import path

from . import views

urlpatterns = [
    path('',views.hello),
    path('one',views.haiThere),
    path('two',views.show)
]