from django.shortcuts import render, redirect
from .models import Articles
from .forms import  ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
# Страница показа всех новостей
def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})

# Страница отображения новости
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

# Страница изменения новости
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    
    form_class = ArticlesForm

# Страница удаления новости
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/delete.html'

# Функция отправки формы с новостью в бд
def create(request):
    # Проверка корректности формы
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)

