from django.urls import path
from .views import students_list, subjects_list

urlpatterns = [
    path('students/', students_list),
    path('subjects/', subjects_list),
]
