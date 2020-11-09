from django.urls import path

from data import views


app_name = 'data'


urlpatterns = [
    path('clinical_research/', views.ClinicalResearch.as_view(), name='clinical_research'),
    path('clinic_data/<int:pk>', views.ClinicalData.as_view(), name='clinic_data'),
    # path('download-xlsx/', views.RateDownloadXLSX.as_view(), name='download-xlsx'),
    path('add_clinic/', views.AddClinic.as_view(), name='add_clinic'),
    path('edit_clinic/<int:pk>', views.EditClinic.as_view(), name='edit_clinic'),
    path('delete_clinic/<int:pk>', views.DeleteClinic.as_view(), name='delete_clinic'),
]
