from django.urls import path

from . import views

urlpatterns = [
    # path('',views.hello),
    path('one',views.haiThere),
    path('two',views.show),
    path('',views.logging),
    path('new',views.callCreate),
    path('home',views.callList),
    path('edit/<int:theone>',views.callEdit),
    path('<int:which>',views.callRead),
    path('del/<int:key>',views.callDelete),
    path('short',views.callShort),
    path('logout',views.callOut)
]

'''path('log',views.logging),
    path('act',views.getting)'''