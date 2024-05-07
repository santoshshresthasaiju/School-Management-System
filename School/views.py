from django.shortcuts import get_object_or_404, render, redirect
from .models import School,SchoolManagement
from .forms import SchoolForm, SchoolManagementForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# views for School.
def school_list(request):
    schools = School.objects.all()

    return render(request, 'School/school_list.html', {'schools':schools})

@login_required(login_url="login")
def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'School created successfully!')
        return redirect('School:school_list')
    else:
        form = SchoolForm()

    return render(request, 'School/school_create.html', {'form': form})

def school_update(request, school_id):
    school = School.objects.get(pk=school_id)
    form = SchoolForm(instance=school)

    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('School:school_list')
    context = {
        'school':school,
        'form':SchoolForm
    }

    return render(request, 'School/school_update.html', context)



def school_delete(school_id):
    school = get_object_or_404(School, pk=school_id)
    school.delete()


    return redirect('School:school_list')


#views for Management

def mgt_list(request):
    mgt = SchoolManagement.objects.all()
    return render(request, 'School/mgt_list.html',{'mgt': mgt})


def mgt_details(request):

    return render(request, 'School/mgt_details.html')

@login_required(login_url="login")
def mgt_create(request):
    if request.method == 'POST':
        form = SchoolManagementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Management created successfully!')
            return redirect('School:mgt_list')
    else:
        form = SchoolManagementForm()

    return render(request, 'School/mgt_create.html', {'form': form})


def mgt_update(request, schoolMgtID):
    mgt = SchoolManagement.objects.get(pk=schoolMgtID)
    form = SchoolManagementForm(instance=mgt)

    if request.method == 'POST':
        form = SchoolManagementForm(request.POST, request.FILES, instance=mgt)
        if form.is_valid():
            form.save()
            return redirect('School:mgt_list')
    context = {
        'mgt':mgt,
        'form':SchoolManagementForm
    }
    return render(request, 'School/mgt_update.html', context)



def mgt_delete(schoolMgtID):
    mgt = get_object_or_404(SchoolManagement, pk=schoolMgtID)
    mgt.delete()
    
    return redirect('School:mgt_list')