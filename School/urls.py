from django.urls import path, include
from . import views

app_name = 'School'

urlpatterns = [
    path('',views.school_list, name="school_list"),
    path('school_create',views.school_create, name="school_create"),
    path('school_update/<int:school_id>',views.school_update, name="school_update"),
    path('school_delete/<int:school_id>',views.school_delete, name="school_delete"),


    #path for schoolManagement
    path('',views.mgt_list, name="mgt_list"),
    path('mgt_create',views.mgt_create, name="mgt_create"),
    path('mgt_update',views.mgt_update, name="mgt_update"),
    path('mgt_delete',views.mgt_delete, name="mgt_delete"),


]
