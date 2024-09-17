from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import AdornmentsEntryForm
from main.models import AdornmentsEntry

# Create your views here.
def show_main(request):
    adornments_entries = AdornmentsEntry.objects.all()

    context = {
        'name': 'Annisa Dwiyanti Ismael',
        'class': 'PBP B',
        'npm': '2306240111',
        'adornments_entries': adornments_entries,
    }

    return render(request, "main.html", context)

def create_adornments_entry(request):
    form = AdornmentsEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_adornments_entry.html", context)

def show_xml(request):
    data = AdornmentsEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AdornmentsEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AdornmentsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AdornmentsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")