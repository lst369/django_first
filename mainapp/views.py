from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница ЛСТ',
        'values': ['some', 'hello', 'my name is ЛСТ'],
        'obj':{
            'bike': 'BMW',
            'age': '25',
            'hobby': 'growing',
        }
    }
    return render(request, 'mainapp/index.html', data )

def about(request):
    return render(request, 'mainapp/about.html')