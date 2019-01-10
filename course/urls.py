from django.urls import path
from .views import (
    CourseUpdateView,
    CourseCreateView,
    CourseListView,
    CourseView,
    my_fbv,
)
app_name = 'course'
urlpatterns = [
    # path('', my_fbv, name='course_list'),
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:id>/', CourseView.as_view(), name='course_details'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:id>/update', CourseUpdateView.as_view(), name='course_update')
]