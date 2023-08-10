from django.urls import  path
from first_apps import views

urlpatterns=[
    path("",views.demo,name="demo_page"),
    path("company",views.first_page,name="first_page"),
    path("employee",views.second_page,name="second_page"),
    path("success",views.success,name="request_done"),
    path("show",views.show_data,name="show"),
    path("show_emp",views.show_data_emp,name="show2"),
    path("update",views.update_data,name="update"),
    path("update_emp",views.update_data_emp,name="update2"),
    path("delete1",views.delete_data,name="delete"),
    path("delete_emp",views.delete_data_emp,name="delete2"),
      path("delete/<int:id>/",views.delete,name="delete3"),
      path("edit/<int:id>",views.edit,name="edit3"),
]