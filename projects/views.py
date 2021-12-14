from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import ProjectForm

from .models import Project

from django.contrib.auth.decorators import login_required

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project.html', context)
   
def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    context = {'project':projectobj}
    return render(request, 'singleproject.html', context)


@login_required(login_url='/users/login/')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'project_form.html', context)


def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        form.is_valid()
        form.cleaned_data
        form.save()
        return redirect('projects')

    context = {'project':project, 'form':form}
    return render(request, 'project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object':project}
    return render(request, 'delete_template.html', context)
