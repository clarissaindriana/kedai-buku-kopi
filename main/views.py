from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306211660',
        'name': 'Clarissa Indriana P',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)