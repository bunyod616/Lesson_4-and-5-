from django.shortcuts import render
from django.views import View
from .models import Student
from django.http import HttpResponse
class StudentListView(View):
    def get(self, request):
        search = request.GET.get('search')

        if not search:
            students = Student.objects.all()
            context = {
                'students': students,
                'search': search
            }
            return render(request, 'student.html',  {'talabalar': students},)
        else:
            students = Student.objects.filter(first_name__icontains=search)
            if students:
                context = {
                    'students': students,
                    'search': search
                }
                return render(request, 'student.html', context)
            else:
                return HttpResponse('<h1>No student found</h1>')


class StudentView(View):
    def get(self, request):
        return render(request, 'index.html')
