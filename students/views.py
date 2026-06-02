from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.db.models import Avg
from django.core.paginator import Paginator


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')




@login_required
def delete_student(request, id):
    student = get_object_or_404(Student,id=id)   
    student.delete()  
    messages.success(request,"student deleted succesfully")               
    return redirect('/')

@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('/')

    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {
        'form': form
    })


@login_required
def student_list(request):

    query = request.GET.get('q', '').strip()   
    course_query=request.GET.get('course','').strip()
    form = StudentForm(request.POST or None,request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,"student added succesfully !")
            return redirect('/')

    student_list= Student.objects.all().order_by('-id')
    if query:
        student_list = student_list.filter(name__icontains=query)
    if course_query:
        student_list = student_list.filter(course__icontains=course_query)

    total_students=student_list.count()
    highest_marks = student_list.order_by('-marks').first()
    average_marks = student_list.aggregate(Avg('marks'))['marks__avg']
    passed_students=Student.objects.filter(marks__gte=35).count()
    failed_students=Student.objects.filter(marks__lt=35).count()
    topper_name=highest_marks.name if highest_marks else "no data"
    filtered_count=student_list.count()

    
    paginator=Paginator(student_list,5)
    page_number=request.GET.get('page')
    students=paginator.get_page(page_number)

    
    return render(request, 'home.html', {
        'students': students,
        'query': query,
        'form': form,
        'total_students':total_students,
        'highest_marks':highest_marks,
        'average_marks':average_marks,
        'passed_students':passed_students,
        'failed_students':failed_students,
        'topper_name':topper_name,
        'filtered_count':filtered_count,
        'course_query':course_query,
    })