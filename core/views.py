from django.shortcuts import render, redirect
from .models import Person

def home(request):
    persons = Person.objects.all()
    return render(request, "index.html", {"persons": persons})

def save(request):
    person_name = request.POST.get("person_name")
    Person.objects.create(name=person_name)
    persons = Person.objects.all()
    return render(request, "index.html", {"persons": persons})

def detail(request, id):
    person = Person.objects.get(id=id)
    return render(request, "update.html", {"person": person})

def update(request, id):
    person_name = request.POST.get("person_name")
    person = Person.objects.get(id=id)
    person.name = person_name
    person.save()
    return redirect(home) 

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)
