from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('add',views.add),
    path('manage',views.manage),
    path('list',views.list),
    path('login',views.custom_login),
    path('logout',views.logout_view),
]
