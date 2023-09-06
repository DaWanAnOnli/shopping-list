from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'William Joel Matthew Quinn Rompis',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
