from django.urls import path, include
from . import views

app_name = 'School'

urlpatterns = [
    path('',views.school_list, name="school_list"),
    path('school_create',views.school_create, name="school_create"),
    path('school_update/<int:school_id>',views.school_update, name="school_update"),
    path('school_delete/<int:school_id>',views.school_delete, name="school_delete"),


    #path for schoolManagement
    path('mgt_list',views.mgt_list, name="mgt_list"),
    path('mgt_create',views.mgt_create, name="mgt_create"),
    path('mgt_update/<int:schoolMgtID>',views.mgt_update, name="mgt_update"),
    path('mgt_delete/<int:schoolMgtID>',views.mgt_delete, name="mgt_delete"),  

    # path for SchoolManagementSchool
    path('sms_list',views.sms_list, name="sms_list"),
    path('sms_create',views.sms_create, name="sms_create"),
    path('sms_update/<int:schoolMgtID>',views.sms_update, name="sms_update"),
    path('sms_delete/<int:schoolMgtID>',views.sms_delete, name="sms_delete"), 


]
