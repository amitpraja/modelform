from django.shortcuts import render
from testapp.form import studentform
from testapp.models import student

# Create your views here.
def stu_view(request):
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/index.html',{'form':form})

def data_view(request):
    form = student.objects.all()
    return render(request,'testapp/data.html',{'form':form})

def ho_view(request):
    return render(request,'testapp/home.html')
