from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Person
from .forms import PersonForm
# Create your views here.


@login_required
def list_clients(request):
    persons = Person.objects.all()
    return render(request, 'list.html', {'persons': persons})


@login_required
def new_client(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_clients')

    return render(request, 'new.html', {'form': form})


@login_required
def update_client(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('list_clients')
    return render(request, 'update.html', {'form': form})


@login_required
def delete_client(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('list_clients')
    return render(request, 'delete.html', {'person_name': person.first_name+' '+person.last_name})


def logout_user(request):
    logout(request)
    return redirect('login')

