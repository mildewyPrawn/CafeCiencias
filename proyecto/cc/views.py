from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect

def index(request):
    '''
    Index View. Para cambiar ir a cc/templates/index
    Es la página en la que este pedo aterriza (landing page).
    '''
    template = 'cc/index.html'
    context = {}
    return render(request, template, context)
class About(View):
    '''
    About View. Para cambiar ir a cc/templates/about
    página con información de nosotros.
    '''
    template_name = 'cc/about.html'
    context = {'title': 'About us'}
    def get(self, request):
        return render(request, self.template_name, self.context)
class OnePost(View):
    '''
    OnePost View. Para ver los posts de la comida, así es como cada post se ve
    TODO: arreglar lo de la imagen
    '''
    template = 'cc/one_post.html'
    context = {}

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.context['post'] = post
        self.context['title'] = str(post)

        return render(request, self.template, self.context)

class HomePageView(ListView):
    '''
    HomePageView View. Para ver un listado de los posts (comidas de los días)
    '''
    model = Post
    template_name = 'cc/list.html'

class CreatePostView(CreateView):
    '''model = Post
    form_class = PostForm
    template_name = 'cc/add.html'
    success_url = reverse_lazy('list')
    '''
    def get(self, request):
        formulario = PostForm()
        contexto = {"formulario": formulario}
        return render(request, 'cc/add.html', contexto)
    def post():
        return HttpResponse("Error al seleccionar")
