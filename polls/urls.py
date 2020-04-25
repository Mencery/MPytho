from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('admin/add_question/', views.add_question, name='add_question'),
    path('admin/edit_question/', views.edit_question, name='edit_question'),
    path('admin/get_statistic/', views.get_statistic, name='get_statistic'),
    path('client/', views.client, name='client'),
    path('client/answer/', views.answer, name='answer'),
]