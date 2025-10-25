from django.urls import path

from . import views

app_name = 'criteria'
urlpatterns = [
    path('', views.index, name='index'),
    path('campus/<int:campus_id>/', views.index, name='index-campus'),
    path('faculty/<int:faculty_id>/', views.index, name='index-faculty'),
    path('project/<int:project_id>/', views.show_project, name='project-index'),
    path('project/<int:project_id>/<int:faculty_id>/', views.show_project, name='project-faculty'),
    path('test/<int:project_id>/', views.test_view, name='test'),   # temp url for testing
]
