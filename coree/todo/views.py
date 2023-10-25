from django.shortcuts import render,redirect
from todo.models import *


def Table(request):
    tasks = Tasks.objects.all()
    inProgress = InProgress.objects.all()
    complete = Complete.objects.all()
    if request.method == 'POST':
        task = request.POST['task']

        Tasks.objects.create(content = task)
        return redirect('Table')
    return render(request,'table.html',{'tasks':tasks, 'inProgress':inProgress,'complete':complete})
    
def moveInProgress(request,id):
    tasks = Tasks.objects.filter(id=id).first()
    InProgress.objects.create(content = tasks.content)
    Tasks.objects.filter(id=id).delete()

    return redirect('Table')

def moveComplete(request,id):
    inprogress = InProgress.objects.filter(id=id).first()
    Complete.objects.create(content = inprogress.content)
    InProgress.objects.filter(id=id).delete()

    return redirect('Table')

def deleteTask(request,id):
    Complete.objects.filter(id=id).delete()
    return redirect('Table')


# Create your views here.
