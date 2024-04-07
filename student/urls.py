from django.urls import path
from .views import StudentView, StudentListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student'),
    path('', StudentView.as_view(), name='landing'),

]