from .forms import PostForm, SignInForm
from .models import Post
from .utils import IsNotAuthenticatedMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView

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

class OnePost(LoginRequiredMixin, TemplateView):

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

class HomePageView(LoginRequiredMixin, TemplateView):
    '''
    HomePageView View. Para ver un listado de los posts (comidas de los días)
    '''
    model = Post
    template_name = 'cc/list.html'

class CreatePostView(LoginRequiredMixin, TemplateView):
    '''
    CreatePostView. Lo usamos para crear un post, solo el admin puede crearlos.
    '''
    
    def get(self, request):
        formulario = PostForm()
        contexto = {"formulario": formulario}
        return render(request, 'cc/add.html', contexto)
    
    def post(self, request):
        formulario = PostForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('../../../list/')
        contexto = {"formulario": formulario}
        return render(request, 'cc/add.html', contexto)

class SignInView(IsNotAuthenticatedMixin ,View):
    """
    Vista para iniciar sesión
    """
    template = 'User/registration/login.html'
    context = {}

    def get(self, request):
        form = SignInForm()
        return render(request, self.template)
    
    def post(self, request):
        """
        Valida y hace el login
        """
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if request.GET.get("next", None) is not None:
                    return redirect(request.GET.get("next"))
                return redirect('/list/')
            form.add_error("username","Usuario o contraseña erroneos.")
            self.context['form'] = form
            return render(request, self.template, self.context)
        return render(request, self.template, self.context)

# TODO: Evitar que se pueda acceder sin loggearse

class LogoutView(LoginRequiredMixin, View):
    """
    Hace el logout, redige a la landing page
    """
    def get(self, request):
        logout(request)
        return redirect("/")
