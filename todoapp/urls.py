from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.employee_list),
    path('list/',views.employee_form)
]