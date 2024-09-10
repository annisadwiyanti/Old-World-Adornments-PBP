from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306240111',
        'name': 'Annisa Dwiyanti Ismael',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)