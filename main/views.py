from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import AdornmentsEntryForm
from main.models import AdornmentsEntry
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'npm': '2306240111',
        'last_login': request.COOKIES.get('last_login', 'Never logged in')  # Menggunakan .get() dengan nilai default
    }

    return render(request, "main.html", context)

def create_adornments_entry(request):
    form = AdornmentsEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        adornments_entry = form.save(commit=False)
        adornments_entry.user = request.user
        adornments_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_adornments_entry.html", context)

def show_xml(request):
    data = AdornmentsEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AdornmentsEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AdornmentsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AdornmentsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_adornments(request, id):
    # Get adornments entry berdasarkan id
    adornments = AdornmentsEntry.objects.get(pk = id)

    # Set adornments entry sebagai instance dari form
    form = AdornmentsEntryForm(request.POST or None, instance=adornments)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_adornments.html", context)

def delete_adornments(request, id):
    # Get adornments berdasarkan id
    adornments = AdornmentsEntry.objects.get(pk = id)
    # Hapus adornments
    adornments.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def products(request):
    # Mengambil data produk untuk menampilkan card
    adornments_entries = AdornmentsEntry.objects.all()
    return render(request, 'products.html', {'adornments_entries': adornments_entries})

def collections(request):
    # Tampilkan lima container pada halaman collections
    return render(request, 'collections.html')

@csrf_exempt
@require_POST
def add_adornments_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    size = strip_tags(request.POST.get("size"))
    color = strip_tags(request.POST.get("color"))
    quantity = request.POST.get("quantity")
    user = request.user

    new_adornments = AdornmentsEntry(
        name=name, price=price,
        description=description,
        size=size, color=color,
        quantity=quantity,
        user=user
    )
    new_adornments.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_adornment_flutter(request):
    if request.method == 'POST':
        # Parse data dari request body
        data = json.loads(request.body)
        
        # Buat entri baru
        new_adornment = AdornmentsEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"],
            size=data["size"],
            color=data["color"],
            quantity=int(data["quantity"]),
        )

        new_adornment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@login_required
def get_user_adornments_json(request):
    # Ambil hanya item yang terasosiasi dengan pengguna yang login
    adornments = AdornmentsEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', adornments), content_type='application/json')