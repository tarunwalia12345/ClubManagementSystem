from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('about/',views.about,name='About'),
    path('registration/',views.showformdata,name='Form'),
    path('status/',views.reqInfo,name='Status'),
    path('student_approve/<str:user_id>', views.student_approve,name="student_approve"),
    path('student_disapprove/<str:user_id>', views.student_disapprove,name="student_disapprove"),
]
 