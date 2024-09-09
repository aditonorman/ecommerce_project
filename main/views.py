from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'E-Commerce App',
        'developer_name': 'Muhammad Raditya Indrastata Norman',
        'class_name': 'KKI',
    }
    return render(request, 'home.html', context)
