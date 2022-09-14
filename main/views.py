from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import studentform
from .models import students


# Create your views here.
def home(request):
    context = {
	'form': studentform(),
	'students': students.objects.all()

	}
    return render(request, 'main/home.html', context)


def form(request):

    context = {
	'form': studentform(),
	}
    return render(request, 'main/form.html', context)

def update_student(request,pk):

    studentobject = students.objects.get(id=pk)
    form = studentform(instance=studentobject)
    context = {
        'form': form,
        'studentobject': studentobject,

    }
    return render(request, 'main/update-student.html', context)



def update_student_store(request, pk):
    studentobject = students.objects.get(id=pk)
    if request.method == 'POST':
        form = studentform(request.POST, instance=studentobject)

        if form.is_valid():
            form.save()
            messages.success(request, f' Student  succesfully Updated')
            return redirect('student-detail', pk=studentobject.id)
        form = studentform(instance=studentobject)
        return render(request, 'main/update-student.html', {'form':form})
        
     


class ListStudents(ListView):
    model = students
    template_name = "main/students.html"
    context_object_name = 'students'


def detailstudent(request, pk):
    studentobject = students.objects.get(id=pk)
    context = {'studentobject': studentobject}
    return render(request, 'main/student-detail.html', context)


@require_http_methods(['POST'])
def add_student(request):
    
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()             
            messages.success(request, f' Student  succesfully Added')
            studentslist = students.objects.all()
            return render(request, 'main/students.html', {'students': studentslist})
        context = {'form': form }
        return render(request, 'main/form.html', context)
            
        


@require_http_methods(['DELETE'])
def delete_student(request,pk):
    studentobj = students.objects.get(id=pk)
    studentobj.delete()
    studentslist = students.objects.all()
    messages.success(request,f' Student  succesfully Deleted')

