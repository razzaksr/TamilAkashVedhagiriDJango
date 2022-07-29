from django.urls import path

from . import views

urlpatterns = [
    path('',views.hello),
    path('one',views.haiThere),
    path('two',views.show),
    path('log',views.logging),
    path('new',views.callCreate)
    
]

'''path('log',views.logging),
    path('act',views.getting)'''