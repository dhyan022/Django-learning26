from django.urls import path
from . import views
urlpatterns = [
    path('marks/',views.marks),
    path('info/',views.info),
    path('teachers/',views.faculty)
]