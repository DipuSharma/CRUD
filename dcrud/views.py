from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect


# Create your views here.
# Add And Show Item form Database code
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    std = User.objects.all()
    return render(request, 'dcrud/addshow.html', {'form': fm, 'data': std})


#  The Function is used for Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This Function is Used for Edit Data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'dcrud/update.html', {'form': fm})
