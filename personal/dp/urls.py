
from django.urls import path

from . import views
from .views import AddPersonView, ViewPersonsView
app_name='dp'


urlpatterns = [

    path('register/',views.register,name="register"),
    path('login/', views.login, name="login"),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name='index'),
    path('add_person/', AddPersonView.as_view(), name='add_person'),
    path('view_persons/', ViewPersonsView.as_view(), name='view_persons'),

]