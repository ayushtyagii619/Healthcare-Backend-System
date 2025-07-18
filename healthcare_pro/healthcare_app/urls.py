from django.urls import path
from .views import RegisterApiView, LoginApiView, PatientCreateApiView, PatientDeatilsApiView, DoctorCreateApiView,DoctorDetailsApiView, MappingCreateApiView, MappingByPatientApiView, MappingDeleteApiView

urlpatterns = [
    path('auth/register/', RegisterApiView.as_view()),
    path('auth/login/', LoginApiView.as_view()),
    path('patients/', PatientCreateApiView.as_view()),
    path('patients/<int:pk>/', PatientDeatilsApiView.as_view()),
    path('doctors/',DoctorCreateApiView.as_view()),
    path('doctors/<int:pk>/',DoctorDetailsApiView.as_view()),
    path('mappings/', MappingCreateApiView.as_view()),
    path('mappings/<int:patient_id>/', MappingByPatientApiView.as_view()),
    path('mappings/delete/<int:pk>/', MappingDeleteApiView.as_view()),
]

