from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Course
from .forms import CourseModelForm
# class CourseView(View):
#     template_name = "course/course_detail.html"
#     def get(self, request, *kargs, **kwargs):
#         print(request.method)
#         return render(request, self.template_name, {})

class CourseUpdateView(View):
    template_name = "course/course_update.html"
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            
        return obj

    def get(self, request, id=None, *kargs, **kwargs):
        print(request.method)
        context = {}

        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
            
        return render(request, self.template_name, context)
    
    def post(self, request, *kargs, **kwargs):      #Do something with the form data on POST submit
        print(request)
        context = {}

        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
            
        return render(request, self.template_name, context)

    def get_success_url(self):
        return reverse('course:course_list')
    

class CourseCreateView(View):
    template_name = "course/course_create.html"
    def get(self, request, id=None, *kargs, **kwargs):
        print(request.method)
        form = CourseModelForm()        #renders the form on GET request
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *kargs, **kwargs):      #Do something with the form data on POST submit
        print(request)
        form = CourseModelForm(request.POST)        #gets the form data into form
        if form.is_valid() :
            form.save()
            form = CourseModelForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def get_success_url(self):
        return reverse('course:course_list')

class CourseListView(View):
    template_name = "course/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context =  {
            'object_list': self.get_queryset()
        }

        return render(request, self.template_name, context)

# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)

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