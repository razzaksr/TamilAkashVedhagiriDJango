from django.urls import path

from . import views

urlpatterns = [
    # path('',views.hello),
    path('one',views.haiThere),
    path('two',views.show),
    path('log',views.logging),
    path('new',views.callCreateOrEdit),
    path('',views.callList),
    path('<int:which>',views.callRead),
    path('edit/<int:theone>',views.callCreateOrEdit)
    
]

'''path('log',views.logging),
    path('act',views.getting)'''