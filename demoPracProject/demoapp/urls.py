from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('policy/', views.policy, name="policy"),
    path('post_employee_details/', views.EmployeeDetailsViewset.as_view({'post': 'create'}), name="post_employee_details"),
]