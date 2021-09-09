from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, Section,Unit, Project
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

def load_sections(request):
    location_id = request.GET.get('location')    
    sections = Section.objects.filter(location_id=location_id).order_by('name')
    context = {'sections': sections}
    return render(request, 'hr/section_dropdown_list_options.html', context)

def load_units(request):
    section_id = request.GET.get('section')    
    units = Unit.objects.filter(section_id=section_id).order_by('name')
    context = {'units': units}
    return render(request, 'hr/unit_ddl.html', context)

def load_projects(request):
    unit_id = request.GET.get('unit')    
    projects = Project.objects.filter(unit_id=unit_id).order_by('name')
    context = {'projects': projects}
    return render(request, 'hr/project_ddl.html', context)
