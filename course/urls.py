from django.urls import path
from .views import (
    # CourseDetailView,
    CourseView,
    my_fbv,
)
app_name = 'course'
urlpatterns = [
    # path('', my_fbv, name='course_list'),
    path('', CourseView.as_view(template_name="contact.html"), name='course_list'),
    path('<int:id>/', CourseView.as_view(), name='course_details')
]