from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .forms import studentform,votesform
from django.db.models import Q
from .models import students,votes


# Create your views here.
def home(request):
    context = {'students': students.objects.all()}
    return render(request, 'main/home.html', context)
    
#canbeused with  pagination
# class home(ListView):
#     model = students
#     template_name = "main/home.html"
#     paginate_by= 3
#     context_object_name = 'students'

def form(request):
    context = {'form': studentform(), }
    return render(request, 'main/form.html', context)


class ListStudents(ListView):
    model = students
    template_name = "main/students.html"
    paginate_by= 5
    context_object_name = 'students'


#@require_http_methods(['POST'])
def add_student(request):

    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f' Student  succesfully Added')
            studentslist = students.objects.all()
            return render(request, 'main/students.html', {'students': studentslist})
        context = {'form': form}
        return render(request, 'main/form.html', context)


def detailstudent(request, pk):
    studentobject = students.objects.get(id=pk)
    votesinfo = votes.objects.filter(studentid=pk)
    likes = votes.objects.filter(studentid=pk,upvoted=1).count()
    dislikes = votes.objects.filter(studentid=pk,upvoted=0).count()
    context = {'studentobject': studentobject,'votesinfo':votesinfo,'likes':likes,'dislikes':dislikes}
    return render(request, 'main/student-detail.html', context)


def update_student(request, pk):
    studentobject = students.objects.get(id=pk)
    form = studentform(instance=studentobject)
    context = {'form': form, 'studentobject': studentobject, }
    return render(request, 'main/update-student.html', context)


def update_student_store(request, pk):
    studentobject = students.objects.get(id=pk)
    if request.method == 'POST':
        form = studentform(request.POST, instance=studentobject)

        if form.is_valid():
            form.save()
            messages.success(request, f' Student  succesfully Updated')
            return redirect('student-detail', pk=studentobject.id)
        context = {'form': form}
        return render(request, 'main/form.html', context)

#still works if you remove these http methods
@require_http_methods(['DELETE'])
def delete_student(request, pk):
    studentobj = students.objects.get(id=pk)
    studentobj.delete()
    studentslist = students.objects.all()
    messages.success(request, f' Student  succesfully Deleted')
    return render(request, 'main/students.html', {'students': studentslist})


def searched_student(request):
    if request.method == 'POST':
        searchedq = request.POST.get('searchedstudent')
        studentslist = students.objects.filter(
            Q(student_firstname__contains=searchedq) |
            Q(student_lastname__contains=searchedq)
        )
        return render(request, 'main/students.html', {'students': studentslist})



@require_http_methods(['POST'])
def vote(request,pk):
    v = votes()
    studentobj = students.objects.get(id=pk)
    v.studentid = studentobj.id
    v.upvoted = 1
    v.save()
    messages.success(request, f' Student  upvoted succesfully ')
    return redirect('student-detail', pk=studentobj.id)

@require_http_methods(['POST'])
def downvote(request,pk):
    v = votes()
    studentobj = students.objects.get(id=pk)
    v.studentid = studentobj.id
    v.upvoted = 0
    v.save()
    messages.success(request, f' Student  downvoted succesfully ')
    return redirect('student-detail', pk=studentobj.id)
        