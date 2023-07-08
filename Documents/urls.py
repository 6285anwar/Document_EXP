from django.contrib import admin
from django.urls import path
from app import views
from app import cloud_function
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('navbar',views.navbar,name="navbar"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('property_save_main',views.property_save_main,name="property_save_main"),
    path('properties',views.properties,name="properties"),
    path('property_view/<int:id>',views.property_view,name="property_view"),
    path('property_save/<int:id>',views.property_save,name="property_save"),
    path('save_property/<int:id>',views.save_property,name="save_property"),
    path('update_property/<int:id>',views.update_property,name="update_property"),
    path('delete_property/<int:id>',views.delete_property,name="delete_property"),
    path('delete_owner/<int:id>',views.delete_owner,name="delete_owner"),


    path('property_user_credentials/<int:id>',views.property_user_credentials,name="property_user_credentials"),
    path('fmc_save/<int:id>',views.fmc_save,name="fmc_save"),
    path('fm_save/<int:id>',views.fm_save,name="fm_save"),
    path('Company_Enhancement_save/<int:id>',views.Company_Enhancement_save,name="Company_Enhancement_save"),
    path('Labour_save/<int:id>',views.Labour_save,name="Labour_save"),
    path('Electronic_Card_save/<int:id>',views.Electronic_Card_save,name="Electronic_Card_save"),
    path('Civil_Defence_save/<int:id>',views.Civil_Defence_save,name="Civil_Defence_save"),
    path('delete_cc/<int:id>',views.delete_cc,name="delete_cc"),




    path('property_document_exp/<int:id>',views.property_document_exp,name="property_document_exp"),
    path('landmap_docsave/<int:id>',views.landmap_docsave,name="landmap_docsave"),
    path('doc_file_save/<int:id>',views.doc_file_save,name="doc_file_save"),


    path('property_staff/<int:id>',views.property_staff,name="property_staff"),
    path('save_staff/<int:id>',views.save_staff,name="save_staff"),

    path('staff_documents_add/<int:id>',views.staff_documents_add,name="staff_documents_add"),

    path('staff_doc_save/<int:id>',views.staff_doc_save,name="staff_doc_save"),



    path('property/<int:id>',views.property,name="property"),
    path('property_update/<int:id>',views.property_update,name="property_update"),


    path('update_property_doc/<int:id>',views.update_property_doc,name="update_property_doc"),
    path('update_staff_doc/<int:id>',views.update_staff_doc,name="update_staff_doc"),

    path('update_staff_doc_save/<int:id>',views.update_staff_doc_save,name="update_staff_doc_save"),


    path('update_staff_file/<int:id>',views.update_staff_file,name="update_staff_file"),
    




    path('company_documents',views.company_documents,name="company_documents"),

#========================= AJAX =========================

    path('ajax_password/',views.ajax_password,name='ajax_password'),





#======================cloudfunction========================

    path('Notify_Email',cloud_function.Notify_Email,name="Notify_Email")

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)