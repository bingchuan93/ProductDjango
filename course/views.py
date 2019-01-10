from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
# class CourseView(View):
#     template_name = "course/course_detail.html"
#     def get(self, request, *kargs, **kwargs):
#         print(request.method)
#         return render(request, self.template_name, {})

class CourseView(View):
    template_name = "course/course_detail.html"
    def get(self, request, id=None, *kargs, **kwargs):
        print(request.method)
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

# Create your views here.
def my_fbv(request, *kargs, **kwargs):
    return render(request, 'about.html', {})