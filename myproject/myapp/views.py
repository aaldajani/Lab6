from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students.html', {'students': students, 'form': form})

def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    available_courses = Course.objects.exclude(students=student)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})



